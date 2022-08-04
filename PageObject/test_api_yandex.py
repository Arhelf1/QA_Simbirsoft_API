from main_page import MainPage


def test_api():
    api = "AQAAAABjhMxtAADLWzXqdww540azlhMPfD7nyss"
    url = "https://cloud-api.yandex.net"
    header = {'Content-Type': 'application/json',
              'Accept': 'application/json', 'Authorization': f'OAuth {api}'}
    l = []
    page = MainPage()
    page.get_resourses(url, header, l)
