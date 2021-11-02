
import requests
import re

from bs4 import BeautifulSoup as BS


RE_STRING = r'<div class="champion-index-table__name">([A-Z][a-z]+\'*[a-zA-Z]+)<\/div>\n\S+\s\S+\n\D+\S+\n\D+\S+\n\D+1\.png"\/>'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.61 Safari/537.36 '
}


class Opgg:

    def __init__(self, url, db):

        self.url = url
        self.db = db
        self.tier_lists = {}

        page = requests.get(url, headers=HEADERS)
        print(f'\nGET request for "{page.url}" responded with status code: {page.status_code}')
        self.status_code = page.status_code
        self.soup = BS(page.content, 'html.parser')

        return

    def find_patch(self):
        result = self.soup.find("div", {"class": "champion-index__version"}).getText()
        patch = re.findall(".* (\d+.\d+)", result)[0]

        return patch

    def build_opgg(self, role, print_flag=False):

        if not str(self.status_code).startswith('2'):
            print_flag and print(f'ABORTING OP.GG WEBSCRAPE: STATUS CODE = {self.status_code}')
            return

        if role == "bot":
            role = "ADC"
        else:
            role = str(role).upper()

        try:
            element = f"tabItem champion-trend-tier-{role}"
            results = self.soup.find("tbody", {"class": element}).find_all("tr")

            champions = re.findall(RE_STRING, str(results))
            self.tier_lists[role.lower()] = champions

            if print_flag:
                print(f"Found Op.gg {str(role).capitalize()} Tier 1 Champions: {champions}" )

        except AttributeError as e:
            print(e)
            # if print_flag:
            #     print(f'SOUP: ${self.soup}')
            # self.build_opgg(role, print_flag)

        return

    def save_opgg(self, params):
        self.db


        return
