from main_page import MainPage


def test_api():
    api = "AQAAAABjef9BAADLW-8eWg6Ogk8YqZewxu36Pxc"
    url = "https://cloud-api.yandex.net"
    header = {'Content-Type': 'application/json',
              'Accept': 'application/json', 'Authorization': f'OAuth {api}'}
    mass = ['Новая папка', 'Файлы для новой папки', 'Горы.jpg', 'Зима.jpg', 'Мишки.jpg', 'Море.jpg',
            'Москва.jpg', 'Санкт-Петербург.jpg', 'Файл для копирования.docx', 'Хлебные крошки.mp4']

    page = MainPage()
    page.get_resourses(url, header, mass)
