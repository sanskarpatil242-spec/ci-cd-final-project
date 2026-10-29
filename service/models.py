"""
Models for Account Service
"""


class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""


class Account:
    """Class that represents an Account"""

    data = {}

    def __init__(self, id=None, name="", email="", address=""):
        self.id = id
        self.name = name
        self.email = email
        self.address = address

    def create(self):
        """Creates an Account in the database"""
        if self.id is None:
            self.id = len(Account.data) + 1
        Account.data[self.id] = self
        return self

    def update(self):
        """Updates an Account in the database"""
        if not self.id or self.id not in Account.data:
            raise DataValidationError("Update called on non-existent account")
        Account.data[self.id] = self
        return self

    def delete(self):
        """Removes an Account from the database"""
        if self.id in Account.data:
            del Account.data[self.id]

    @classmethod
    def all(cls):
        """Returns all Accounts in the database"""
        return list(cls.data.values())

    @classmethod
    def find(cls, account_id):
        """Finds an Account by its ID"""
        return cls.data.get(account_id)

    def serialize(self):
        """Serializes an Account into a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
        }

    def deserialize(self, data):
        """Deserializes an Account from a dictionary"""
        try:
            self.name = data["name"]
            self.email = data["email"]
            self.address = data.get("address", "")
        except KeyError as err:
            raise DataValidationError("Invalid Account: missing " + err.args[0])
        return self
