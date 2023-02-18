class Product:

    CATEGORIES = ["Beverages", "Bread/Bakery", "Canned/Jarred Goods", "Dairy", "Dry/Baking Goods", "Frozen Foods", "Meat", "Produce", "Cleaners", "Paper Goods", "Personal Care", "Other"]

    def __init__(self, code, name, price, category):
        self.code = code
        self.name = name
        self.price = price
        self.category = category

    def get_code(self):
        """Retrieve a code from a specific product

        Returns:
            String: Product code
        """
        return self.code
    
    def get_name(self):
        """Retrieve a name from a specific product

        Returns:
            String: Product name
        """
        return self.code

    def get_price(self):
        """Retrieve a price from a specific product

        Returns:
            Float: Product price
        """
        return self.code

    def get_category(self):
        """Retrieve a category from a specific product

        Returns:
            String: Product category
        """
        return self.code

    def set_name(self, name):
        """Update a name of a specific product

        Args:
            name (String): Product name
        """
        self.name = name

    def set_price(self, price):
        """Update a price of a specific product

        Args:
            price (String): Product price
        """
        self.price = price
    
    def set_category(self, category):
        """Update a category of a specific product

        Args:
            category (String): Product category
        """
        self.category = category

    def __str__(self) -> str:
        #return f"{self.name}({self.age})"
        return f"Product code: {self.code}, Name: {self.name}, Price: {self.price}, Category: {self.category}"


p1 = Product("XD133","Coke 1Lt", 3.54, "Drinks")
print(p1)
p1.set_price(5)
print(p1)