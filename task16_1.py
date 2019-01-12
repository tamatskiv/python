#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.codeabbey.com/index/user_ranking").content
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('tr')

with open('out.csv', 'w') as s:
    s.write('Number,Username,Language,Rank,Enlightenment,Solved\n')

    for row in table[2:]:
        result = row.get_text().split()
        result = [_.replace(',', '') for _ in result]
        result = ','.join(result)
        s.write(result + '\n')