import requests
from bs4 import BeautifulSoup
import json

def price_rimi(url):
    response = requests.get(url)

    # Check if response is good
    if response.status_code == 200:

        # Parse response through bs4
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.prettify()

        # Find the relevant object
        script_tag = soup.find("script", {"data-cookieconsent": "statistics"})
        old_price_element = soup.find("p", class_="price__old-price")

        script_content = script_tag.string
            
        start_index = script_content.find("{")
        end_index = script_content.rfind("}") + 1
        json_data = script_content[start_index:end_index]

        data = json.loads(json_data)
        impressions = data.get("ecommerce", {}).get("impressions", [])

        # Retrieve price
        product_price = impressions[0].get("price")

        # Check if a discount exists and retrieve it
        if old_price_element:
            discount_price = old_price_element.text.strip()
            discount_price = discount_price[:-1]
            product_price, discount_price = discount_price, product_price
        else:
            discount_price = ''
        return (product_price, discount_price)

    else:
        # Error handling
        print('Failed to fetch the webpage.')
        return None