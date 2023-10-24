import requests
from bs4 import BeautifulSoup
import pprint


def hacker_news(page):
    if page >= 2:
        response = requests.get(f'https://news.ycombinator.com/news?p={page}')
    else:
        response = requests.get('https://news.ycombinator.com/news')

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    return {'links': links, 'subtext': subtext}


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext, score=100):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.select('a')[0].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= score:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def read_news(page, score):
    hn = []
    for i in list(range(page + 1))[1:]:
        news = hacker_news(i)
        custom_news = create_custom_hn(news['links'], news['subtext'], score)
        hn = [*custom_news, *hn]
    return sort_stories_by_votes(hn)
