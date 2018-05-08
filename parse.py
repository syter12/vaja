from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import requests


def prvo():
    req = Request('http://getjoan.com', headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html.parser')
    name = "Joan"

    results = soup.find_all(string=re.compile('.*{0}.*'.format(name)), recursive=True)
    print('Found the word "{0}" {1} times\n'.format(name, len(results)))

def drugo():
    url = 'http://getjoan.com'
    the_word = 'Joan'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find_all(text=lambda text: text and the_word in text)
    print(words)
    count = len(words)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))

def main():
    prvo()
    drugo()
if __name__ == '__main__':
    main()

