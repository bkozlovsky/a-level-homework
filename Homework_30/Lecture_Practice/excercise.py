"""
ЧАСТЬ 1

Написать класс Product принимающий два параметра имя и цена. Создать три вида покупателя. Просто покупатель, вип и супервип. Три разных класса, которые наследутся друг от друга.

У всех покупателей должен быть бюджет (принимать на вход).

У всех классов должен быть метод, который принимает объект продукта, а в ответ говорит сколько продуктов может купить клиент.

У вип покупателя скидка 20%

У супервипа - еще 20% от предыдущего.

Классам покупателей передавать инстансы класса продукта

ЧАСТЬ 2
Валидация:
- отрицательный бюджет и цена
- тип данных float
- проверка что передается класс продукт методу покупателя

Сложность 1)
Добавить класс VIPProduct наследованный от Product, на него скидка не расспростаняется
Сложность 2)
Сделать возможность задавать скидку при инициализации продукта (Если не задана, оставить 20%)
Сложность 3)
Добавить информацию о кол-ве продуктов на складе, добавить покупателям метод купить продукт(или несколько) , при покупке у клиента должен уменьшатся бюджет, а у продукта уменьшать кол-во на складе
Сложность 4)
Дописать возможность добавлять продукты на склад, и пополнять бюджет клиента
"""

class Product:
    def __init__(self, name, price, inStock, discounted=True):
        self.name = name
        self.price = price
        self._inStock = inStock
        self.discounted = discounted

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v):
        if (isinstance(v, float) and v > 0) == True:
            self._price = v
        else:
            raise Exception('Please input correct price')

    @property
    def inStock(self):
        return self._inStock

    @inStock.setter
    def inStock(self, n):
        if (isinstance(n, int) and n > 0) ==  True:
            self._inStock += n
        else:
            raise Exception("Incorrect amount")

    def addToStock(self, amount):
        if isinstance(amount, int):
            self.inStock += amount
            return f"Successfully added to stock. Currently {self.inStock} items of {self.name} available"
        else:
            raise Exception("Amount of products in incorrect, please double-check")

class VipProduct(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discounted = False

class Buyer:
    def __init__(self, name, budget, discount=1):
        self.name = name
        self.budget = budget
        self.discount = discount

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, b):
        if (isinstance(b, int) or isinstance(b, float)) == True and (b > 0) == True:
            self._budget = b
        else:
            raise Exception("Your balance cannot be negative")

    def get_discount(self, product):
        if product.discounted == True:
            return product.price * self.discount
        else:
            return product.price

    def products_to_buy(self, product):
        amount = self.budget / self.get_discount(product)
        return round(int(amount))

    def purchase(self, product, amount):
        if self.budget < product.price:
            raise Exception("You don't have enough money")
        elif product.inStock < amount:
            raise Exception(f"Not enough products in stock. Only {product.inStock} items of {product.name} available")
        else:
            self.budget -= (product.price * amount)
            product.inStock -= amount
            return f"You got {amount} items of {product.name}\n\nYour remaining balance is {self.budget}"

class VipBuyer(Buyer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discount = 0.8


class SuperVipBuyer(VipBuyer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discount = 0.6


p1 = Product("bread", 18.99, 25)
p2 = Product("sugar", 9.99, 40)
p3 = VipProduct("crabs", 20.99, 500)

buyer = Buyer("Bogdan", 1000)
vip_buyer = VipBuyer("Sergey", 2000)
super_vip_buyer = SuperVipBuyer("Vasya", 3000)

def print_info():
    print(f"\n----------Buyers Summary----------\n")
    print(f"{buyer.name} has {round((1 - buyer.discount) * 100)}% discount. {buyer.name} can get {buyer.products_to_buy(p1)} items of {p1.name}, {buyer.products_to_buy(p2)} items of {p2.name} or {buyer.products_to_buy(p3)} items of {p3.name}.")

    print(f"{vip_buyer.name} has {round((1 - vip_buyer.discount) * 100)}% discount. {vip_buyer.name} can get {vip_buyer.products_to_buy(p1)} items of {p1.name}, {vip_buyer.products_to_buy(p2)} items of {p2.name} or {vip_buyer.products_to_buy(p3)} items of {p3.name}.")

    print(f"{super_vip_buyer.name} has {round((1 - super_vip_buyer.discount) * 100)}% discount. {super_vip_buyer.name} can get {super_vip_buyer.products_to_buy(p1)} items of {p1.name}, {super_vip_buyer.products_to_buy(p2)} items of {p2.name} or {super_vip_buyer.products_to_buy(p3)} items of {p3.name}.")

    print(f"\n----------Products Summary----------\n")
    print(f"{(p1.name).title()} costs {p1.price} for one item. There are {p1.inStock} items in stock.")

    print(f"{(p2.name).title()} costs {p2.price} for one item. There are {p2.inStock} items in stock.")

    print(f"{(p3.name).title()} costs {p3.price} for one item. There are {p3.inStock} items in stock.")

print_info()