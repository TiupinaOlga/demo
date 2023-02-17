import requests
from pprint import pprint


def get_token():
    with open('token.txt', 'r') as file:
        return file.readline()




headers = {'Content-type': 'application/json', 'Authorization': get_token()}

params = {'path': 'text.txt'}

res = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)

json_response = res.json()
pprint(json_response)
href_ = json_response['href']
# print(href_)

params = {'path': 'text.txt', 'url': f'{href_}'}

res_2 = requests.put('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)

json_response_2 = res_2.json()
print(res_2) #202 - файл принят сервером, но еще не был перенесен непосредственно в Яндекс.Диск.
pprint(res_2.json())
