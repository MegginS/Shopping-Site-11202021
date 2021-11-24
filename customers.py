"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
        """Method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name} {self.last_name}>")

def read_customer_info_from_file(filepath):
    """Read customer information and populate dictionary.

    Dictionary will be {email: Customer object}
    """

    customer_list = {}

    with open(filepath) as file:
        for line in file:
            (
            first_name,
            last_name,
            email,
            password,
            ) = line.strip().split("|")


            customer_list[email] = Customer(
                first_name,
                last_name,
                email,
                password,
                )

    return customer_list
        
        
def get_by_email(email):
    """Return a customer, given the email."""

    # This relies on access to the global dictionary `customer_list`

    return customer_list[email]

customer_list = read_customer_info_from_file("customers.txt")