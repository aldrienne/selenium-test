"""
Author: Aldrienne Maniti
Description: Scrape Lazada.com.ph for list of monitors. Lists the monitor name, rating and price.
List of details will be encoded to a csv file.
"""
# Selenium tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# from selenium import webdriver
from Product import Product
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time

import csv

product_list = []

# STEP 1 LOCATE CHROME DRIVER
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
# STEP 2 SPECIFY BROWSER DRIVER
driver = webdriver.Chrome(PATH)
# STEP 3 ACCESS URL
driver.get('https://www.lazada.com.ph/')

# STEP 4 QUERY SEARCH BAR ELEMENT AND ENTER KEYWORD
search = driver.find_element_by_id('q')
search.send_keys("Monitor")
search.send_keys(Keys.RETURN)

# STEP 5 QUERY LIST OF PRODUCTS BY CLASS NAME
try:
    container = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c1_t2i"))
    )

    products = container.find_elements_by_class_name('c5TXIP')

    for product in products:
        rating = WebDriverWait(product, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'c15YQ9'))
        )
        temp_product_name = product.find_element_by_class_name('c16H9d')
        temp_price = product.find_element_by_class_name('c3gUW0')
        try:
            temp_product_rating = product.find_element_by_css_selector('span.c3XbGJ')
        except Exception as e:
            temp_product_rating = '(0)'
        # STEP 6 ADD QUERIED PRODUCT TO LIST
        temp_product = Product(
            product_name=temp_product_name,
            product_price=temp_price,
            product_rating=temp_product_rating

        )
        product_list.append(temp_product)

except Exception as e:
    print(e)

driver.close()

# STEP 7 OUTPUT QUERIED PRODUCTS ON A CSV FILE WITH I/O
with open('output.csv', 'w+', encoding='utf-8') as monitor_file:
    fieldnames = ['monitor_name', 'monitor_price', 'monitor_rating']
    writer = csv.DictWriter(monitor_file, fieldnames=fieldnames)

    writer.writeheader()
    for product in product_list:
        writer.writerow({
            'monitor_name': product.product_name,
            'monitor_price': product.product_price,
            'monitor_rating': product.product_rating
        })

print("FINISHED!")
