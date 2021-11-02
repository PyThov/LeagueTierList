
import requests
import re
from bs4 import BeautifulSoup as BS

# Empty string at end here is to prevent index error when retrieving support data.
ROLES = ["top", "jungle", "mid", "adc", "support", ""]


class Mobalytics:

    def __init__(self, url, db):

        self.url = url
        self.db = db
        page = requests.get(url)

        self.soup = BS(page.content, 'html.parser')
        self.tier_lists = {}

        return

    def build_mobalytics(self, role, print_flag=False):

        results = self.soup.find(attrs={"class": "tier-list"}).findAll(attrs={'class': "section"})
        # print(results)
        if role == 'bot':
            temp_role = 'adc'
        else:
            temp_role = role

        # champions = re.findall(r'<div class="css-bygw6y e3q069b5">\s*([A-Z][a-z]+\'*[a-zA-Z]+)\s*<.div>', str(results))
        role_subset = re.findall(rf'<h3 \S+{temp_role.lower().capitalize()}[\s\S]+<\/div>\s<\/div>, <div class="section">\s<h3 class="{ROLES[ROLES.index(temp_role.lower()) + 1]}', str(results))
        # print(role_subset)
        champions = re.findall(r'width="70"\/>([A-Z][a-z]+\'*[a-zA-Z]+)<'
                               r'', str(role_subset))

        # print(f"\nHTML:\n{results.prettify()}")
        if print_flag:
            print(f"Found Mobalytics {str(temp_role).capitalize()} S-Tier Champions: {champions}")

        self.tier_lists[role.lower()] = champions

        return
