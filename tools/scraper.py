from bs4 import BeautifulSoup
import requests

URL = "https://www.bing.com/images/search?q=penguin"


def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    i = [i['src2'] for i in images if i.has_attr('src2')]


if __name__ == '__main__':
    main()
