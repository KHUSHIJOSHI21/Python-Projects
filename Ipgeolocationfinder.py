import requests
def detect_info(IP):
    api_key="791e70c7eb29e1"
    url=f"https://ipinfo.io/{IP}/json?token={api_key}"
    response=requests.get(url)
    data=response.json()
    print(f"IP:{data['ip']}")
    print(f"Country{data['country']}")
    print(f"City:{data['city']}")
    loc=data['loc']
    latitude,longitude=loc.split(',')
    print(f"Latitude:{latitude}")
    print(f"Longitude:{longitude}")
def main():
    IP=input("Enter the IP Address")
    detect_info(IP)
if __name__=="__main__":
    main()