
"""
Tier list averages
"""


import os
import common

if not os.path.exists('.init_flag.txt'):
    print("NO INIT FLAG")
    common.install_dependencies(True)
    

import math
import plotly.graph_objects as go

from datetime import date
from Opgg import Opgg
from Mobalytics import Mobalytics
from Ugg import Ugg


UGG_URLS = {
    "top": "https://u.gg/lol/top-lane-tier-list",
    "jungle": "https://u.gg/lol/jungle-tier-list",
    "mid": "https://u.gg/lol/mid-lane-tier-list",
    "bot": "https://u.gg/lol/adc-tier-list",
    "support": "https://u.gg/lol/support-tier-list"
}


URLS = {"opgg": "https://na.op.gg/champion/statistics#",
        "mobalytics": "https://mobalytics.gg/blog/lol-tier-list-for-climbing-solo-queue/",
        # "mobalytics": "https://app.mobalytics.gg/lol/tier-list",
        "ugg": UGG_URLS
        }

ROLES = ['top', 'jungle', 'mid', 'bot', 'support']

S_TIER = 3


class LeagueTierList:

    def __init__(self):

        self.urls = URLS
        self.tier_list = {}

        self.opgg = Opgg(URLS["opgg"])
        self.mobalytics = Mobalytics(URLS["mobalytics"])
        self.ugg = Ugg(URLS["ugg"])

        return

    def sort_lists(self):

        for r in ROLES:
            self.tier_list[r] = dict(sorted(self.tier_list[r].items(), key=lambda item: item[1], reverse=True))

        return

    def create_graph(self):

        return

    def create_table(self, role):

        self.sort_lists()

        champions = list(self.tier_list[role].keys())
        counts = list(self.tier_list[role].values())

        fig = go.Figure(data=[go.Table(header=dict(values=['Champion', 'Count']),
                                       cells=dict(values=[champions, counts]))
                              ])
        fig.show()

        return

    def create_s_tier_table(self):
        self.sort_lists()

        # roles = [role.upper() for role in ROLES]
        roles = []
        champions = {}

        print(self.tier_list)
        for role in ROLES:
            roles.append(role.capitalize())
            champions[role] = [f'{str(champs[0])} - {str(champs[1])}' for champs in self.tier_list[role].items() if champs[1] >= S_TIER-1]
            # champions[role] = [champs for champs in self.tier_list[role]][0:5]  # Pull the top 5 champs from the list

            '''if len(champions[role]) == 0:
                champions[role] = ['MOVING TO T2']
                champions[role] += [champs[0] for champs in self.tier_list[role].items() if champs[1] == S_TIER-1]'''

            if len(champions[role]) == 0:
                champions[role] = ['NO DECENT CHAMPS']

        print(champions)

        fig = go.Figure(data=[go.Table(header=dict(values=roles),
                                       cells=dict(values=list(champions.values()))
                                       )])
        fig.show()

        return

    def build_tier_list(self, role):

        self.tier_list[role] = {}

        for champion in self.opgg.tier_lists["adc" if role == "bot" else role]:
            self.tier_list[role][champion] = 1

        for champion in self.ugg.tier_lists[role]:
            if self.tier_list.get(role, {}).get(champion) is None:
                self.tier_list[role][champion] = 1
            else:
                self.tier_list[role][champion] += 1

        for champion in self.mobalytics.tier_lists[role]:
            if self.tier_list.get(role, {}).get(champion) is None:
                self.tier_list[role][champion] = 1
            else:
                self.tier_list[role][champion] += 1

        return

    @staticmethod
    def print_line(message="", length=42, character="-", upper_space=True, lower_space=True):

        if upper_space:
            print()

        for _ in range(length):
            if _ == math.floor(length/2):
                print(message, end="")

            print(character, end="")

        if lower_space:
            print()

        return

    def print_tier_list(self):

        print()

        temp = open(f'tier_lists/overall_tier_list_{date.today().strftime("%Y-%m-%d")}.txt', 'w+')

        self.print_line("OVERALL TIER LIST")
        for x in self.tier_list.keys():
            tmpstr = f"{str(x).lower().capitalize()}: "\
                     f"{dict(sorted(self.tier_list[x].items(), key=lambda item: item[1], reverse=True))}\n"
            print(tmpstr)
            temp.write(tmpstr)

        print()
        temp.close()

    def print_each_tier_list(self):

        print()

        self.print_line("OP.GG")
        for x in self.opgg.tier_lists.keys():
            print(f"{str(x).lower().capitalize()}: {self.opgg.tier_lists[x]}")

        self.print_line("U.GG")
        for x in self.ugg.tier_lists.keys():
            print(f"{str(x).lower().capitalize()}: {self.ugg.tier_lists[x]}")

        self.print_line("MOBALYTICS")
        for x in self.mobalytics.tier_lists.keys():
            print(f"{str(x).lower().capitalize()}: {self.mobalytics.tier_lists[x]}")

        print()
