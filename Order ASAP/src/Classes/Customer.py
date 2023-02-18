class Customer:
    def __init__(self, id, name, lastname, birthdate):
        self.id = id,
        self.name = name,
        self.lastname = lastname,
        self.birthdate = birthdate
    
    def get_id(self):
        """Retrieve a id from a specific customer

        Returns:
            String: Customer id
        """
        return self.id
    
    def get_name(self):
        """Retrieve name

        Returns:
            String: name
        """
        return self.name
    
    def get_lastname(self):
        """Retrieve lastname

        Returns:
            String: lastname
        """
        return self.lastname
    
    def get_birthdate(self):
        """Retrieve birthdate

        Returns:
            String: birthdate
        """
        return self.birthdate
    
    def set_name(self, name):
        """Update name

        Args:
            name (String): name
        """
        self.name = name
    
    def set_lastname(self, lastname):
        """Update name

        Args:
            name (String): lastname
        """
        self.lastname = lastname
    
    def set_birthdate(self, birthdate):
        """Update birthdate

        Args:
            name (Date): birthdate
        """
        self.lastname = birthdate