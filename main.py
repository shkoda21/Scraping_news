import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://www.nj.com/news/')
soup = BeautifulSoup(res.text, 'html.parser')
links1 = soup.select('.river-item__headline--large-screens > a')
links2 = soup.select('.two-box-item__headline--large-screens > a')
subtext1 = soup.select('.river-item__meta')
subtext2 = soup.select('.two-box-item__meta')



def sort_stories_by_time(hnlist):
    return sorted(hnlist, key=lambda k: k['time_publicate'])


def create_custom_hn(links1, subtext1):
    hn = []
    for index, item in enumerate(links1):
        title = item.getText()
        href = item.get('href', None)
        time_publ = subtext1[index].select('.river-item__timestamp')
        if len(time_publ):
            points = time_publ[0].getText().replace(' ago', '')
            if points[-1] == 'h':
                points = int(points[0:-1]) # delete h
            elif points[-1] == 'm':
                points = 0
            if points < 4:
                hn.append({'title': title, 'link': href, 'time_publicate': points})
    return sort_stories_by_time(hn)


def create_custom_hn2(links2, subtext2):
    hn2 = []
    for index, item in enumerate(links2):
        title = item.getText()
        href = item.get('href', None)
        time_publ = subtext2[index].select('.two-box-item__timestamp')
        if len(time_publ):
            points = time_publ[0].getText().replace(' ago', '')
            if points[-1] == 'h':
                points = int(points[0:-1]) # delete h
            elif points[-1] == 'm':
                points = 0
            if points < 4:
                hn2.append({'title': title, 'link': href, 'time_publicate': points})
    return sort_stories_by_time(hn2)


pprint.pprint(create_custom_hn(links1, subtext1) + create_custom_hn2(links2, subtext2))
