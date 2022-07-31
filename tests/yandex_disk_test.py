import json
from handlers import disk_handler


def test_list_of_names():
    data = json.loads(disk_handler.get_resourses().text)
    data = data['_embedded']['items']
    for element in data:
        print(element['name'])
