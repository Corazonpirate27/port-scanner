import socket
from rich.console import Console

console = Console()

def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def main():
    target = input("Enter IP to scan: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080, 8443]
    console.print(f"\n[bold blue]Scanning {target}...[/bold blue]\n")
    for port in ports:
        if scan_port(target, port):
            console.print(f"[green]  [OPEN]  Port {port}[/green]")
        else:
            console.print(f"[red] [CLOSED] Port {port}[/red]")
if __name__ == "__main__":
    main()
