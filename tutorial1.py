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

product_list = []

#STEP 1 LOCATE CHROME DRIVER
PATH = 'C:\Program Files (x86)\chromedriver.exe'
#STEP 2 SPECIFY BROWSER DRIVER
driver = webdriver.Chrome(PATH)
#STEP 3 ACCESS URL
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


for product in products:
    temp_product = Product(
        product_name=product.find_element_by_class_name('c16H9d').text,
        product_price=product.find_element_by_class_name('c3gUW0').text,
    )

    product_list.append(temp_product)

driver.close()

with open('output.txt','w+',encoding='utf+8') as file:
    for product in product_list:
        file.write(product.get_product())

print("FINISHED!")

