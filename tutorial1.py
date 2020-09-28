"""
Author: Aldrienne Maniti
Description: Scrape Lazada.com.ph for list of monitors. Lists the monitor name, rating and price. List of details will be encoded to a csv file.
"""
# Selenium tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from Product import Product
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import csv

product_list = []

# STEP 1 LOCATE CHROME DRIVER
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# STEP 2 SPECIFY BROWSER DRIVER
driver = webdriver.Chrome(PATH)
# STEP 3 ACCESS URL
driver.get('https://www.lazada.com.ph/')

search = driver.find_element_by_id('q')
search.send_keys("Monitor")
search.send_keys(Keys.RETURN)

try:
    container = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c1_t2i"))
    )

    products = container.find_elements_by_class_name('c2prKC')


except Exception as e:
    print(e)

try:
    rating = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.CLASS_NAME,'c3XbGJ'))
    )

    print(driver.page_source)

    for product in products:
        rating_x = product.find_element_by_class_name('c3XbGJ')
        temp_product = Product(
            product_name=product.find_element_by_class_name('c16H9d').text,
            product_price=product.find_element_by_class_name('c3gUW0').text,
            product_rating=rating.find_element_by_css_selector('c3XbGJ')
        )

        product_list.append(temp_product)

except Exception as e:
    print(e)



driver.close()

with open('output.csv', 'w+', encoding='utf-8') as monitor_file:
    fieldnames = ['monitor_name','monitor_price','monitor_rating']
    writer = csv.DictWriter(monitor_file, fieldnames=fieldnames)

    writer.writeheader()
    for product in product_list:
        writer.writerow({
            'monitor_name': product.product_name,
            'monitor_price': product.product_price,
            'monitor_rating': product.product_rating
        })

#Samsung Ls24F350Fhexxp  23.6  Vga/Hdmi Black Monitor
print("FINISHED!")
