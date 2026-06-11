import requests

url = "https://www.ajio.com/s/ham-gold-coins-and-bars-4775-71731?query=%3Aprce-asc"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=30)

print("STATUS:", r.status_code)
print(r.text[:5000])
