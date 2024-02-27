from scrapers import iki_scraper
from scrapers import maxima_scraper
from scrapers import rimi_scraper
from concurrent.futures import ThreadPoolExecutor

# Format all of the functions to use with TPE
def get_iki_info(url):
    return iki_scraper.product_info_iki(url)

def get_maxima_info(url):
    return maxima_scraper.price_maxima(url)

def get_rimi_info(url):
    return rimi_scraper.price_rimi(url)

urls = [
    'https://lastmile.lt/product/IKI/Gaivusis-gazuotas-gerimas-PEPSI-15-l', 
    'https://www.barbora.lt/produktai/gazuotas-gerimas-pepsi-1-5-l-1-5-l', 
    'https://www.rimi.lt/e-parduotuve/lt/produktai/gerimai/gaivieji-gerimai/gazuoti-vaisvandeniai/gaivusis-gerimas-pepsi-1-5l/p/1360378'
]

# Run all 3 scripts at once to optimize time
with ThreadPoolExecutor() as executor:
    iki_info_future = executor.submit(get_iki_info, urls[0])
    maxima_info_future = executor.submit(get_maxima_info, urls[1])
    rimi_info_future = executor.submit(get_rimi_info, urls[2])

# Retrieve the values from output
product_name_iki, product_id_iki, product_price_iki, product_discount_iki, about_info_iki, photo_url_iki, conversion_value_iki, origin_country_iki, ingredients_iki, nutrition_iki, producer_iki, storing_conditions_iki, supplier_iki, taxes_iki = iki_info_future.result()
product_price_maxima, product_discount_maxima = maxima_info_future.result()
product_price_rimi, product_discount_rimi = rimi_info_future.result()

# Find the optimal price from all stores
if product_discount_iki != '':
    iki_price = product_discount_iki
else:
    iki_price = product_price_iki

if product_discount_rimi != '':
    rimi_price = product_discount_rimi
else:
    rimi_price = product_price_rimi

if product_discount_maxima != '':
    maxima_price = product_discount_maxima
else:
    maxima_price = product_price_maxima

front_price = min(iki_price, min(maxima_price, rimi_price))

print("Iki:", iki_price, "Maxima:", maxima_price, "Rimi:", rimi_price)
print(front_price)
