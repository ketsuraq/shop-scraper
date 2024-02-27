import requests
from bs4 import BeautifulSoup
import json

def product_info_iki(url):
    response = requests.get(url)

    # Check if response is good
    if response.status_code == 200:

        # Parse the response through bs4
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.prettify()

        # Find the relevant object
        script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
        script_content = script_tag.string
        data = json.loads(script_content)

        # Retrieve all of the information
        product_name = data['props']['pageProps']['product']['name']['lt']
        product_id = data['props']['pageProps']['product']['id']
        product_price = data['props']['pageProps']['product']['prc']['p']
        product_discount = data['props']['pageProps']['product']['prc']['s']
        about_info = data['props']['pageProps']['product']['description']['lt']
        photo_url = data['props']['pageProps']['product']['photoUrl']
        conversion_value = data['props']['pageProps']['product']['conversionValue']
        origin_country = data['props']['pageProps']['product']['countryOfOrigin']
        ingredients = data['props']['pageProps']['product']['ingredients']['lt']
        nutrition = data['props']['pageProps']['product']['nutrition']
        producer = data['props']['pageProps']['product']['producer']
        storing_conditions = data['props']['pageProps']['product']['storingConditions']['lt']
        supplier = data['props']['pageProps']['product']['supplier']
        taxes = data['props']['pageProps']['product']['taxes']['deposit']
        
        return (product_name, product_id, product_price, 
                product_discount, about_info, photo_url, 
                conversion_value, origin_country, ingredients, 
                nutrition, producer, storing_conditions, supplier, taxes)

    else:
        # Error handling
        print('Failed to fetch the webpage')