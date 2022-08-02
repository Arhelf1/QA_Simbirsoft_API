import json
import requests


class MainPage():

    def get_resourses(self, url_, header, mass, lis, path="%2f", lvl=0):
        if lvl == 0:
            print('Список файлов и папок:')
        response = requests.request(
            method="GET", url=f"{url_}/v1/disk/resources?path=" + path, headers=header)
        data = json.loads(response.text)
        data = data['_embedded']['items']
        for element in data:
            print(lvl*'   '+element['name'])
            lis.append(element['name'])
            if "." not in element['name']:
                self.get_resourses(
                    url_, header, mass, lis, path+element['name']+'%2f', lvl+1)
            # print(lis)
        # lis == mass
# TODO Разбить метод еще на несколько методов
