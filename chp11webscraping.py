#!/usr/bin/env python3
import bs4, requests

# res = requests.get('https://www.amazon.co.uk/PS4-PRO-Red-Dead-Redemption/dp/B07HKV4TR4/ref=sr_1_1?s=videogames&ie=UTF8&qid=1541109558&sr=1-1&keywords=ps4+pro')
# print(res.raise_for_status)

# soup = bs4.BeautifulSoup(res.text, 'html.parser') # Returns a soup object.
# elems = soup.select('#priceblock_dealprice')
# print(elems)
# print(elems[0].text.strip())

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status() #Check for an exception if there is a problem downloading this
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text #Removes whitespace to get our price

price = getAmazonPrice('https://www.amazon.co.uk/Nintendo-Switch-Super-Ultimate-Download/dp/B07HFQ46LS/ref=sr_1_7?s=videogames&ie=UTF8&qid=1541112710&sr=1-7&keywords=nintendo+switch')
print('The price of this product is ' + price + '.')




    