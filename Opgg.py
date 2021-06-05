
import requests
import re

from bs4 import BeautifulSoup as BS


RE_STRING = r'<div class="champion-index-table__name">([A-Z][a-z]+\'*[a-zA-Z]+)<\/div>\n\S+\s\S+\n\D+\S+\n\D+\S+\n\D+1\.png"\/>'


class Opgg:

    def __init__(self, url):

        self.url = url
        self.tier_lists = {}

        page = requests.get(url)
        self.soup = BS(page.content, 'html.parser')

        return

    def build_opgg(self, role, print_flag=False):

        # print(f"Attempting to find tier list on {self.url}")

        if role == "bot":
            role = "ADC"
        else:
            role = str(role).upper()

        element = f"tabItem champion-trend-tier-{role}"
        try:
            results = self.soup.find("tbody", {"class": element}).find_all("tr")

            champions = re.findall(RE_STRING, str(results))
            self.tier_lists[role.lower()] = champions

            if print_flag:
                print(f"Found Op.gg {str(role).capitalize()} Tier 1 Champions: {champions}")

        except AttributeError:
            self.build_opgg(role, print_flag)

        return
