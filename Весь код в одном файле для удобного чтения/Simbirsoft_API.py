import requests
import json

api = "AQAAAABjef9BAADLW-8eWg6Ogk8YqZewxu36Pxc"
_url = "https://cloud-api.yandex.net"
header = {'Content-Type': 'application/json',
          'Accept': 'application/json', 'Authorization': f'OAuth {api}'}


def get_resourses():
    response = requests.request(
        method="GET", url=f"{_url}/v1/disk/resources?path=%2F", headers=header)
    data = json.loads(response.text)
    return data['_embedded']['items']


def main():
    data = get_resourses()
    for element in data:
        print(element['name'])


if __name__ == "__main__":
    main()
