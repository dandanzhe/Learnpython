from bs4 import BeautifulSoup
import re
import urllib2
Url = 'https://www.codewars.com/users/leaderboard'


def solution(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(),'html.parser',from_encoding='utf-8')
    data = soup.find('div',class_='leaderboard pan')
    return data
print solution(Url)