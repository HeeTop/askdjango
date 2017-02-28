import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','askdjango.settings')
import django
django.setup()
from webcrawler.models import BlogData


def parse_blog():
    url='https://beomi.github.io/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'lxml')
    mytitles = soup.select('h3 > a')
    data={}
    for mytitle in mytitles:
        data[mytitle.text] = mytitle.get('href')
    return data


# 이 명령어는 import가 아닌 파이썬에서 직접 실행할 경우 동작함
if __name__ == '__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()


