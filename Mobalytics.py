
import requests
import re
from bs4 import BeautifulSoup as BS


class Mobalytics:

    def __init__(self, url):

        page = requests.get(url)

        self.soup = BS(page.content, 'html.parser')
        self.url = url
        self.tier_lists = {}

        return

    def build_mobalytics(self, role, print_flag=False):

        results = self.soup.find(id=f"{role}-anchor-id").find(attrs={'data-sel-id': "ChampionsSBlock"})
        champions = re.findall(r'<div class="css-bygw6y e3q069b5">\s*([A-Z][a-z]+\'*[a-zA-Z]+)\s*<.div>', str(results))

        # print(f"\nHTML:\n{results.prettify()}")
        if print_flag:
            print(f"Found Mobalytics {str(role).capitalize()} S-Tier Champions: {champions}")

        self.tier_lists[role.lower()] = champions

        return
