import bs4, requests

def getamazonprice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#product-price-1990 > span')
    return elems[0].text.strip()




price = getamazonprice('https://www.pcaskin.com/products-by-skin-concern/acne/acne-cream.html')
print('The price is ' + price)



