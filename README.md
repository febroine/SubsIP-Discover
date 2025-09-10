# SubdomainScanner 🌐

A Python tool for subdomain enumeration and HTTP status checking.  
It uses a wordlist to generate potential subdomains, resolves their IPs, and optionally performs HTTP requests to detect active services.

---

## 🚀 Features

- Reads subdomains from a wordlist (`subs.txt`)
- Resolves each subdomain to its IP address
- Saves live subdomains and IPs to `sonuc.txt`
- Checks for common HTTP response codes (200, 301, 302, 403)
- Progress display with real-time percentage updates
- Colored output in the terminal for better readability

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies using:

```bash
pip install requests
```

## 📂 File Structure

subs.txt: Wordlist of subdomains (one per line)

sonuc.txt: Output file where found subdomains/IPs and HTTP statuses are written

## ⚙️ Example Usage

```bash
$ python subs-ip_discover.py
Alan adını girin: example.com
```
## 📄 Output

Found results will be saved in sonuc.txt:
```bash
Bulundu: www.example.com - IP: 93.184.216.34
[+] www.example.com (93.184.216.34) - HTTP Yanıt Kodu: 200

```
## ⚠️ Legal Usage

This tool is provided for educational and authorized penetration testing purposes only.
Do not scan or interact with domains you do not own or have permission to test. Unauthorized use may be illegal.
