# coding:utf-8
# https://www.codewars.com/kata/581c06b95cfa838603000435/train/python
from bs4 import BeautifulSoup
import requests
Url = 'https://www.codewars.com/users/leaderboard'

class user(object):
    def __init__(self, name, clan, honor):
        super(user, self).__init__()
        self.name = name
        self.clan = clan
        self.honor = honor
class Leaderboard(object):

    def __init__(self, position):
        self.position = position

def solution():
    response = requests.get(Url).content
    soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
    data = soup.find('div', class_="leaderboard pan")
    res = data.find_all('td')
    flag = len(res) / 4
    position = {}
    for i in range(flag):
        position[i + 1] = user(res[i * 4 + 1].find('a').contents[1], res[i * 4 + 2].contents, res[i * 4 + 3].contents)
        # print res[i*4].text
        # print res[i*4+1].find('span').contents
        # print res[i*4+1].find('a').text
        # print res[i*4+2].contents
        # print res[i*4+3].contents
        # print positions[i+1].name
    return Leaderboard(position)
# leaderboard = solution()
# print leaderboard.position[1].name