from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import re
import os
import datetime

print('Finding images...')

try:
    html = urlopen('https://unsplash.com')
    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll('a', {'href': re.compile('/.*download')})

    abs_links = []
    for link in links:
        abs_links.append(str('https://unsplash.com' + link['href']))
    abs_links = list(set(abs_links))

    print('Found {} images.'.format(len(abs_links)))
    print('Downloading images...')

    base_path = os.getcwd()
    today_string = re.search("(^.{4}-.{2}-.{2})", str(datetime.datetime.now())).group(0)

    for index, img_link in enumerate(abs_links):
        file_path = 'unsplash-' + today_string + '-' + str(index + 1) + '.jpeg'
        out_path = os.path.join(base_path, file_path)
        urlretrieve(img_link, out_path)

except Exception as e:
    print('Something went wrong:')
    print(e)
