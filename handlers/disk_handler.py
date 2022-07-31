import imp
from settings import token
import requests

_url = "https://cloud-api.yandex.net"
header = {'Content-Type': 'application/json',
          'Accept': 'application/json', 'Authorization': f'OAuth {token.api}'}


def get_resourses():
    response = requests.request(
        method="GET", url=f"{_url}/v1/disk/resources?path=%2F", headers=header)
    return response
