import geocoder
from geopy.geocoders import ArcGIS
from geopy.geocoders import Nominatim
import os
import time


def check_ip(ip, geocoder, geolocator):
    g = geocoder.ip(ip)
    location = geolocator.reverse((g.lat, g.lng), language='zh-CN')
    return location.address + '\n'

def get_unique_filename(filename):
    base, ext = os.path.splitext(filename)
    suffix = 1
    while os.path.exists(filename):
        filename = f"{base}_{suffix}{ext}"
        suffix += 1
    return filename

def main():
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    save_filename = get_unique_filename('results.txt')
    f = open(save_filename, 'w', encoding="utf-8")
    r = open("ip_list.txt")
    lines = r.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace('：', ':')
        line = line.replace(' ', '')
        line = line.replace('：', ':')
        if line == "":
            continue
        print(line)
        result = check_ip(line, geocoder, geolocator)
        print(result)
        time.sleep(1)
        f.write(line + '\n')
        f.write(result)

if __name__ == '__main__':
    main()
