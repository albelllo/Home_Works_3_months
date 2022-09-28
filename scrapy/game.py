import requests
from bs4 import BeautifulSoup as BS

URL = "https://multoigri.ru/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def get_requests(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data_game(html):
    soup = BS(html,  "html.parser")
    items = soup.find_all("a", class_='games-list_game-link')
    game = []

    for item in items:
        game.append(
            {
                "image": URL + item.find("img").get("src"),
                "link": URL + item.find("link", itemprop='url').get("href"),

            }
        )
    return game



def scrapy_script_game():
    html = get_requests(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 3):
            html = get_requests(f"https://multoigri.ru/?page={page}")
            anime.extend(get_data_game(html.text))
        return anime
    else:
        raise Exception("Error in scrapy script function")
