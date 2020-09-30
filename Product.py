

class Product:
    """A Class to represent a product.

    Attributes
    ----------
    product_name : str
        name of the product
    product_price: str
        price of the product
    product_rating
        number of rating

    Methods
    ----------
    get_product():
        Takes in all product attributes and converts into a 1 line string with delimiter of \t
        Returns:
            product details(str)

    """
    def __init__(self, product_name, product_price, product_rating='0'):
        """Constructs all necessary  attributes of the product
            Parameters
                product_name : str
                    name of the product
                product_price: str
                    price of the product
                product_rating
                    number of rating
                    rating will be set to 0 if not available
        """
        self.product_name = str(product_name)
        self.product_price = str(product_price)
        self.product_rating = str(product_rating).replace('(', '').replace(')', '')

    def get_product(self):
        """
        Takes in all product attributes and converts into a 1 line string
        Returns:
            product details(str)
        """
        return str(self.product_name + '\t' + self.product_rating + '\t' + self.product_price)
