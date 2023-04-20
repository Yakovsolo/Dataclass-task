"""Create a dataclass named "Product" that has the following attributes:
    product_id: int
    name: str
    price: float
    quantity: int
The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.
Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost."""


from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self) -> float:
        return round(self.price * self.quantity, 2)


def find_highest_total_cost(products) -> "Product":
    highest_cost_product = None
    highest_total_cost = 0
    for product in products:
        total_cost = product.total_cost()
        if total_cost > highest_total_cost:
            highest_total_cost = total_cost
            highest_cost_product = product
    return highest_cost_product


products_list: List[Product] = []

number_of_products = int(input("Please input a number of products:\n"))

for number in range(number_of_products):
    product_id = number + 1
    print(f"\nproduct id: {product_id}")
    name = input("Please input product name:\n")
    price = float(input("Please input a price:\n"))
    quantity = float(input("Please input a quantity:\n"))
    products_list.append(
        Product(product_id=product_id, name=name, price=price, quantity=quantity)
    )


for product in products_list:
    print(
        f"{product.product_id}. {product.name}:\nprice: {product.price}$\nquantity: {product.quantity}"
    )

highest_cost_product = find_highest_total_cost(products_list)
print(
    f"\nThe product with the highest total cost is {highest_cost_product.name} "
    f"with a total cost of {highest_cost_product.total_cost()}$"
)
