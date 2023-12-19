import requests
from bs4 import BeautifulSoup

def get_rss(url):
    topic = []
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')        
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            description = a.find('description').text
            article = {
                'title': title,
                'link': link,
                'published': published,
                'description': description
                }
            topic.append(article)
        return topic
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)