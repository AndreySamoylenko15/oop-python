class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price


    def show_info(self):
        print(self.name, self.price)


    def discount(self, amount):
        self.price -= amount

    def is_expensive(self):
        return self.price > 20


product1= Product('Milk', 30)
product2= Product(name='Bread', price=25)
product3= Product(name='Apple', price=10)


products= [product1, product2, product3]


for product in products:
    if product.is_expensive():
        product.show_info()

product1.show_info()
product1.discount(10)
product1.show_info()