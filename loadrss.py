from argys.wsgi import application
from django.db import transaction
from info.models import News, Org
import feedparser
import datetime
import time


def load_news():
    org = Org.objects.get(pk=1)
    data = feedparser.parse(org.rss)
    begin_date = datetime.datetime.today().replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    news_links = list(News.objects.filter(pubDate__gt=begin_date).values_list('link', flat=True))
    with transaction.atomic():
        for item in data.entries:
            if item.link not in news_links:
                news = News()
                news.title = item.title
                news.link = item.link
                news.pubDate = datetime.datetime.fromtimestamp(time.mktime(item.published_parsed))
                news.save()


if __name__ == '__main__':
    load_news()
