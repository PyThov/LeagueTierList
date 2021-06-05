
import re
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException as SNCE

RE_STRING = r'\n\d+\n([A-Z][a-z]+\'*[a-zA-Z]+)\nS\+*\n\d+\.\d*%\n\d+\.\d*%\n\d+\.\d*%\n\d+,\d+'

OPTIONS = webdriver.ChromeOptions()
CAPABILITIES = {'browserName': 'chrome', 'version': '89', 'platform': 'ANY'}


class Ugg:

    def __init__(self, urls):

        self.urls = urls
        self.tier_lists = {}

        try:
            self.browser = Chrome('D:\\Documents\\Chrome\\chromedriver.exe', desired_capabilities=CAPABILITIES)
        except SNCE as e:
            print(e)
            print("UPDATING CHROMEDRIVER VERSION")


        return

    def build_ugg(self, role, print_flag=False):

        # print(f"Query {self.urls[role]} for tier list...")
        self.browser.get(self.urls[role])
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        page = self.browser.find_element_by_class_name("content-section")

        # print(page.text)
        champions = re.findall(RE_STRING, page.text)
        self.tier_lists[role.lower()] = champions

        if print_flag:
            print(f"Found u.gg {str(role).capitalize()} S-Tier Champions: {champions}")

        return
