import requests


def ip_lookup():
    try:
        ip_til_scan = input("Indtast din ip du vil slå op her: ")
        api_url = f"http://ip-api.com/json/{ip_til_scan}"

        data = requests.get(api_url).json()
    
        land = data['country']
        region = data['regionName']
        by = data['city']
        tidszone = data['timezone']
        isp = data['isp']
        print ("Land: " + str(land))
        print("Region: " + str(region))
        print("By: " + str(by))
        print("Tidszone: " + str(tidszone))
        print("ISP: " + str(isp))
    except:
        print("IP ADRESSEN FINDES IKKE!")