import requests
from bs4 import BeautifulSoup


class TpbApi():
    def __init__(self, url="https://thepiratebay.se"):
        self.url = url

    def search(self, query):
        t = requests.get(self.url + '/search/' + query + '/0/99/0')
        soup = BeautifulSoup(t.text, 'lxml')

        return self.parse(soup)

    def parse(self, soup):
        results = []
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            i = 0

            # print(tds[1])

            name = tds[1].find_all('a', {
                "class": "detLink"
            }, href=True)[0].text

            magnet = tds[1].find_all('a', {
                "title": "Download this torrent using magnet"
            }, href=True)[0]['href']

            seeders = tds[2].text

            size = tds[1].find_all('font', {
                "class": "detDesc"
            })[0].text.split()

            size = size[4] + size[5]
            size = size.replace(',', '')

            d = {
                "name": name,
                "size": size,
                "magnet": magnet,
                "seeders": seeders
            }

            results.append(d)

        return results

if __name__ == '__main__':
    t = TpbApi()
    k = t.search('matrix')
    print(k)
