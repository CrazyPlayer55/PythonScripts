import requests
from bs4 import BeautifulSoup

term = "270880"
baseurl = "https://store.steampowered.com/search/?term=" + term + "&ignore_preferences=1"

r = requests.get(baseurl)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('span', class_='title')
print(title.text.strip())

date = str(soup.find('div', class_='col search_released responsive_secondrow'))
print('Released on ' + date[54:66].replace('<', ''))

if soup.find('strike') != None:
    oldPrice = str(soup.find('strike'))
    newPrice = str(soup.find('div', class_='col search_price discounted responsive_secondrow'))
    discount = str(soup.find('div', class_='col search_discount responsive_secondrow'))
    #print(oldPrice, discount[6:10], newPrice)
else:
    price = str(soup.find('div', class_='col search_price responsive_secondrow'))
    if len(price) == 108:#$1-$9
        print(price[77:82])
    elif len(price) == 109:#$10-$99
        print(price[77:83])
    elif len(price) == 110:#$100-$999
        print(price[77:85])
    elif len(price) == 115:#Free To Play
        print(price[77:89])
    elif len(price) == 107:#Free
        print(price[77:81])
