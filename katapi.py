import requests
from bs4 import BeautifulSoup


class KatApi():
    def __init__(self, url="https://kat.cr/"):
        self.url = url

    def search(self, query):
        t = requests.get(self.url + 'usearch/' + query)
        soup = BeautifulSoup(t.text, 'lxml')

        return self.parse(soup)

    def parse(self, soup):
        results = []
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')

            if tds == []:
                pass
            else:
                name = tds[0].find_all('a', {
                    "class": "cellMainLink"
                }, href=True)[0].text

                magnet = tds[0].find_all('a', {
                    "title": "Torrent magnet link"
                }, href=True)[0]["href"]

                seeders = tds[4].text

                size = tds[1].text

                d = {
                    "name": name,
                    "size": size,
                    "magnet": magnet,
                    "seeders": seeders
                }

                results.append(d)

        return results
