class Request:

    class_counter= 0

    def __init__(self, quantity, product):
        self.quantity = quantity
        self.product = product
        self.idz = Request.class_counter
        Request.class_counter += 1

    def get_idx(self):
        """Retrieve idx

        Returns:
            Int: idx
        """
        return self.idz
    
    def get_product(self):
        """Retrieve product

        Returns:
            Product: product
        """
        return self.product
    
    def get_quantity(self):
        """Retrieve quantity

        Returns:
            Int: quantity
        """
        return self.quantity
    
    def set_product(self, product):
        """Update product

        Args:
            product (Product): product
        """
        self.product = product

request0 = Request(2,"coke")
request1 = Request(1,"pepsi")
print("hola")
print(f"Request 1 id is {request1.get_product()} a")
print(f"Request 1 id is {request1.get_idx()} a")