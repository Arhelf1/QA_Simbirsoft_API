from main_page import MainPage


def test_api():
    api = "AQAAAABjhMxtAADLWzXqdww540azlhMPfD7nyss"
    url = "https://cloud-api.yandex.net"
    header = {'Content-Type': 'application/json',
              'Accept': 'application/json', 'Authorization': f'OAuth {api}'}
    mass = ['Files', 'New', 'NEW', 'Горы.jpg', 'Зима.jpg', 'Мишки.jpg', 'Море.jpg', 'Москва.jpg', 'Санкт-Петербург.jpg', 'Новая презентация.pptx', 'Новая таблица.xlsx',
            'Новый документ.docx', 'Горы.jpg', 'Зима.jpg', 'Мишки.jpg', 'Море.jpg', 'Москва.jpg', 'Санкт-Петербург.jpg', 'Файл для копирования.docx', 'Хлебные крошки.mp4']
    l = []
    page = MainPage()
    page.get_resourses(url, header, mass, l)
