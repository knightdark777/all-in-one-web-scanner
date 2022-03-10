import socket
import requests
import json

hostname = socket.gethostname()
my_ip_address = socket.gethostbyname(hostname)

# protocol_version = str(input("\nHTTPS or HTTP: "))
target_url = str(input("Enter target website: "))
target_ip_address = socket.gethostbyname(target_url)

print("\n<----- Finding The IP Address Of The Target ----->")
print("Your device hostname is " + hostname + " and IP Address is " + my_ip_address)
print("The IP Address of " + target_url + " is " + target_ip_address)

print("\n<----- Banner Grabbing Of The Target ----->")

req = requests.get("https://" + target_url)
print(str(req.headers))

req_two = requests.get("https://ipinfo.io/" + target_ip_address + "/json")
resp_ = json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])

print("\n<----- Finding All The Subdomains Of The Target ----->")
file = open("subdomain-wordlist.txt", "r")
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    # url = f"http://{subdomain}.{target_url}"
    try:
        requests.get(f"http://{subdomain}.{target_url}")
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", f"http://{subdomain}.{target_url}")
