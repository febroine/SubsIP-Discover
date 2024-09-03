import requests
import socket

GREEN = "\033[92m"
RESET = "\033[0m"

with open("subs.txt", "r") as file:
    subdomains = [line.strip() for line in file]

domain = input("Alan adını girin: ")

found_subdomains = []
found_ips = []

total_subdomains = len(subdomains)
processed = 0

with open("sonuc.txt", "w") as result_file:
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found_subdomains.append(subdomain)
            found_ips.append(ip)
            print(f"{GREEN} Bulundu: {subdomain} - IP: {ip}{RESET}")
            result_file.write(f"Bulundu: {subdomain} - IP: {ip}\n")
        except socket.gaierror:
            pass
        
        processed += 1
        progress = (processed / total_subdomains) * 100
        print(f"İlerleme: %{progress:.2f} tamamlandı", end="\r")

    print("\nHTTP yanıt kodlarını kontrol etme:")
    for subdomain, ip in zip(found_subdomains, found_ips):
        try:
            response = requests.get(f"http://{ip}", timeout=5)
            if response.status_code in [200, 301, 302, 403]:
                print(f"{GREEN} {subdomain} ({ip}) - HTTP Yanıt Kodu: {response.status_code}{RESET}")
                result_file.write(f"[+] {subdomain} ({ip}) - HTTP Yanıt Kodu: {response.status_code}\n")
        except requests.exceptions.RequestException:
            pass
