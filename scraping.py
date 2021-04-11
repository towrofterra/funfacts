import requests as rq
from bs4 import BeautifulSoup
page = rq.get('https://www.thefactsite.com/top-100-random-funny-facts/').text
bs = BeautifulSoup(page, features='html.parser')
facts = bs.find(class_="entry-content mt-4 pt-4 border-t").find_all('h2')
for fact in facts:
    print(fact.text)





