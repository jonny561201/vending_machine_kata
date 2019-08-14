class ProductService:

    def __init__(self, database):
        self.database = database
        self.products = None

    def is_product_available(self, selection):
        self.products = self.database.get_product_by_location(selection)
        return len(self.products) > 0

    def get_product_cost(self, selection):
        if self.products is None:
            self.products = self.database.get_product_by_location(selection)
        if len(self.products) > 0 :
            return self.products[0]['cost']
        return 0
