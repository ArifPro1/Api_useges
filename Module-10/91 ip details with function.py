import requests

def res_data(url):
    res =  requests.get(url)
    if res.status_code == 200:
        data = res.json()
    return data





api_find_url = 'https://api.ipify.org?format=json'

data = res_data(api_find_url)
ip = data.get('ip')

# res = requests.get(api_find_url)
# if res.status_code == 200:
#     data = res.json()

ip_location = f'https://ipapi.co/{ip}/json/'
# r = requests.get(ip_location)
# if r.status_code == 200:
#     ip_details = r.json()

ip_details = res_data(ip_location)
city = ip_details.get('city')
region = ip_details.get('region')
country_name = ip_details.get('country_name')

Sentence = f'IP({ip}) located in {city} {region},{country_name}'
print(Sentence)