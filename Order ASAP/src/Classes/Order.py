from datetime import datetime

class Order:
    class_counter= 0
    def __init__(self, customer, coupon, tax_rate):
        self.id = Order.class_counter,
        self.customer = customer,
        self.date = datetime.now(),
        self.coupon = coupon
        self.requests = {}
        Order.class_counter += 1

    def get_id(self):
        """Retrieve id

        Returns:
            String: id
        """
        return self.id

    def get_customer(self):
        """Retrieve customer

        Returns:
            String: customer
        """
        return self.customer
    
    def get_date(self):
        """Retrieve date

        Returns:
            String: date
        """
        return self.date

    def get_coupon(self):
        """Retrieve coupon

        Returns:
            String: coupon
        """
        return self.coupon
    
    def get_requests(self):
        """Retrieve requests

        Returns:
            String: requests
        """
        return self.requests