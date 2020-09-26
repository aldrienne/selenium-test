from selenium import webdriver

class Product:
    """Class for creating product elment"""
    def __init__(self,product_name, product_price,product_rating='0'):
        self.product_name = str(product_name)
        self.product_price = str(product_price)
        self.product_rating = str(product_rating)

    def __str__(self):
        return self.product_name + '\t' + self.product_rating + '\t' + self.product_price

    def get_product(self):
        return str(self.product_name + '\t' + self.product_rating + '\t' + self.product_price + '\n')