import requests
from bs4 import BeautifulSoup
import json

def price_maxima(url):
    response = requests.get(url)

    # Check if response is good
    if response.status_code == 200:

        # Parse the response through bs4
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.prettify()

        # Find the relevant element
        product_div = soup.find("div", {"class": "b-product-info b-product--js-hook"})
        data_b_units = product_div.get("data-b-units")
        data_b_units_json = json.loads(data_b_units)
        data = data_b_units_json["units"][0]
        
        # Retrieve price
        product_price = data['price']

        # Check if a discount exists and retrieve it
        try:
            discount = ''
            discount = data['retail_price']
            product_discount = product_price
            product_price = discount
        except KeyError:
            # Error handling
            product_discount = ''

        return (product_price, product_discount)


    else:
        # Error handling
        print('Failed to fetch the webpage')