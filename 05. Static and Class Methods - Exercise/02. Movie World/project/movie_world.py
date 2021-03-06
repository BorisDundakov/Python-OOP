from project.customer import Customer

from project.dvd import DVD




class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id, dvd_id):
        dvd: DVD = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
        customer: Customer = list(filter(lambda _: _.id == dvd_id, self.customers))[0]
        print("DVD", dvd)
        print("customer", customer)

        if dvd.id in [d.id for d in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        if dvd.is_rented:
            return "DVD is already rented"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer: Customer = list(filter(lambda _: _.id == dvd_id, self.customers))[0]
        if dvd_id in [d.id for d in customer.rented_dvds]:
            dvd: DVD = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        customers = "\n".join([c.__repr__() for c in self.customers])
        dvds = "\n".join([d.__repr__() for d in self.dvds])
        result += customers
        result += dvds
        return result


