import json
import requests


class MainPage():

    def get_resourses(self, url_, header, mass):
        print()
        response = requests.request(
            method="GET", url=f"{url_}/v1/disk/resources?path=%2F", headers=header)
        data = json.loads(response.text)
        l = []
        data = data['_embedded']['items']
        print('Список файлов и папок:')
        for element in data:
            print('   '+element['name'])
            l.append(element['name'])
        l == mass

# TODO Разбить метод еще на несколько методов
