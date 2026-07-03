import socket

print("=" * 50)
print("        PORT STATUS CHECKER")
print("=" * 50)

host = input("Enter Website or IP Address: ")

try:
    ip = socket.gethostbyname(host)

    print(f"\nHost Name : {host}")
    print(f"IP Address: {ip}\n")

    ports = [20,21,22,23,25,53,80,110,143,443,3306,8080]

    for port in ports:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} : OPEN")
        else:
            print(f"Port {port} : CLOSED")

        sock.close()

except socket.gaierror:
    print("Invalid Host")

except KeyboardInterrupt:
    print("\nScan Stopped")
