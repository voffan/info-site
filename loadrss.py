from argys.wsgi import application
from django.db import transaction
from info.models import News, Org
import feedparser
import datetime
import time
import os


def load_news():
    strings = '===============' + datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S") + '===========================\n'
    org = Org.objects.get(pk=1)
    data = feedparser.parse(org.rss)
    begin_date = datetime.datetime.today().replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    news_links = list(News.objects.filter(pubDate__gt=begin_date).values_list('link', flat=True))
    for item in data.entries:
        try:
            if item.link not in news_links:
                news = News()
                news.title = item.title
                news.link = item.link
                news.pubDate = datetime.datetime.fromtimestamp(time.mktime(item.published_parsed))
                news.save()
                strings += 'Успешно загружена новость: ' + item.link + '\n'
        except Exception as e:
            strings += 'Произошла ошибка при загрузке строки ' + str(item) + '\n'
            continue
    with open(os.path.join('logs', datetime.datetime.today().strftime("%d.%m.%Y")+'.txt'), 'a') as f:
        f.write(strings)


if __name__ == '__main__':
    load_news()
