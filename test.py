# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 07:08:17 2024

@author: Tanishq Salkar
"""
# importing necessary libraries
import json
import pandas as pd
from collections import namedtuple

# class product, defined name,id, price and quantity
class Product:
    #initializing the variables passed
    def __init__(self, id:int,name, price: float, quantity:int) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    #function to convert product to dictionary, used later with save function to store data in json file
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    
    
class Inventory:
    #initializing vairiables, storing id's in a set so that there is no repetation, loading data from json file for the inventory
    def __init__(self):
        f = open('data.json')
        self.data = json.load(f)
        self.inventory_items = []
        self.ids = set()
        for product_i in self.data:
            prod = Product(**product_i)
            self.inventory_items.append(prod)
            self.ids.add(prod.id)
    #adding new product to inventory, if id is repeated then the product wont be added
    def add_item(self,product:Product) -> None:
        """Add product"""
        if product.id in self.ids:
            print("product id already present")
        else:
            self.inventory_items.append(product)
            self.ids.add(product.id)
            print(f"Product {product.name} added...")
    
    # removing product from the inventory, correct id is needed
    def remove_item(self,id):
        if id in self.ids:
            index =0
            for item in self.inventory_items:
                if id == item.id:
                    break
                index+=1
            self.ids.discard(self.inventory_items[index].id)
            item = self.inventory_items.pop(index)
            print(f"Item {item.name} removed from dictionary")
            
        else:
            print(f"no item in inventory with item id: {id}")
            
    # func to update price of exisiting item in the inventory
    def update_price(self,id,new_price):
        if id in self.ids:
            index = 0
            for item in self.inventory_items:
                if id == item.id:
                    break
                index+=1
            self.inventory_items[index].price = new_price
            print(f"Product { self.inventory_items[index].name} updated new price {self.inventory_items[index].price}")
        else:
            print(f"no item in inventory with item id: {id}")
    
    # func to update quantity of exisiting item in the inventory
    def update_quantity(self,id,new_quantity):
        if id in self.ids:
            index = 0
            for item in self.inventory_items:
                if id == item.id:
                    break
                index+=1
            self.inventory_items[index].quantity = new_quantity
            print(f"Product { self.inventory_items[index].name} updated new quantity {self.inventory_items[index].quantity}")
        else:
            print(f"no item in inventory with item id: {id}")
    
    # func to update price and quantity of exisiting item in the inventory
    def update_price_quantity(self,id,new_price,new_quantity):
        if id in self.ids:
            index = 0
            for item in self.inventory_items:
                if id == item.id:
                    break
                index+=1
            self.inventory_items[index].price = new_price
            self.inventory_items[index].quantity = new_quantity
            print(f"Product { self.inventory_items[index].name} updated new quantity {self.inventory_items[index].quantity} new price {self.inventory_items[index].price}")
        else:
            print(f"no item in inventory with item id: {id}")
    
    # function to list all the items present in the inventory
    def list_products(self):
        print("*****************************************************************************")
        for product_i in self.inventory_items:
            print(f"ID: {product_i.id} Item:{product_i.name}  Price: {product_i.price} Quantity:{product_i.quantity}")
        print("*****************************************************************************")
    
    # function to get specific id in inventory, id is needed
    def specific_item(self,id):
        if id in self.ids:
            for product_i in self.inventory_items:
                if id == product_i.id:
                    print(f"ID: {product_i.id} Item:{product_i.name}  Price: {product_i.price} Quantity:{product_i.quantity}")
                    break
        else:
            print(f"no item in inventory with item id: {id}")

    # func to alert about less items in the inventory, will be generated based on the min quantity passed
    def low_stock_alert(self,min_quantity):
        for product_i in self.inventory_items:
            if product_i.quantity< min_quantity:
                print(f"ID: {product_i.id} Item:{product_i.name}  Price: {product_i.price} Quantity:{product_i.quantity}")
    
    # function to generate overall report of items in inventory along with total items and total value
    def total_inventory_value(self):
        total_value = 0
        total_items = 0
        print("Inventory Report")
        print("******************************************************************")
        for product_i in self.inventory_items:
            total_product_cost = product_i.quantity * product_i.price
            total_items +=  product_i.quantity
            total_value += total_product_cost
            print(f"Product {product_i.name} total value: {total_product_cost}")
        print("******************************************************************")
        print(f"Total Items in Inventory {total_items} having value {total_value}")
        
    # to store transactions made to the inventory before exiting the code
    def save_data(self):
        products = []
        for item in self.inventory_items:
            products.append(item.to_dict())
        with open('data.json', 'w') as f:
            json.dump(products,f, indent=4)
        print("saving data............")


def main():
    # creating the inventory object
    inventory = Inventory()
    counter = 0 
    
    # using while loop to take user response and genrate outptu
    while True:
        if counter==0:
            # list of functions user can perform
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Product")
            print("5. List All Products")
            print("6. Low-Stock Alert")
            print("7. Total Inventory Value")
            print("8. Exit")
            counter +=1
            
        choice = input("Enter your choice: ")
        
        # code to add new product
        if choice == '1':
            id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product = Product(id, name, price, quantity)
            inventory.add_item(product)
            
        # code to update new product
        elif choice == '2':
            id = int(input("Enter Product ID to update: "))
            print("1. Update Price")
            print("2. Update Quantity")
            print("3. Update Price and Quantity")
            update_choice = input("Enter your choice: ")

            if update_choice == '1':
                new_price = float(input("Enter new price: "))
                inventory.update_price(id, new_price)
            elif update_choice == '2':
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(id, new_quantity)
            elif update_choice == '3':
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_price_quantity(id, new_price, new_quantity)
            else:
                print("Invalid choice")
        # to delete a product
        elif choice == '3':
            id = int(input("Enter Product ID to delete: "))
            inventory.remove_item(id)
        # to view details of a product
        elif choice == '4':
            id = int(input("Enter Product ID to view: "))
            inventory.specific_item(id)
        # print all the products in inventory
        elif choice == '5':
            inventory.list_products()
            
        # low stock alret based on min quantity you pass
        elif choice == '6':
            min_quantity = int(input("Enter minimum quantity for low-stock alert: "))
            if min_quantity<0:
                print("Invalid quantity entered.....")
                print("Try again.....")
            inventory.low_stock_alert(min_quantity)
        
        # to generate the inventory report
        elif choice == '7':
            inventory.total_inventory_value()
            
        # to exit the function
        elif choice == '8':
            inventory.save_data()
            print("Exiting the program.")
            break
        
        # if invalid number is entered by the user
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
          
          
          
          