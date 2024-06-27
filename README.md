# Inventory_management_project

## Class Product
The project contains two class Product and Inventory

In Class Product, I have defined attributes such as id, name price and quantity.

It also has function to_dict(), whuch returns all the attributes of the product class as a dictionary key value pair.

## Class Inventory 

In Inventory class, I am initializing the list which contains all the products and their respective attributes. Also loading and storing the data into json object.

Also product id are stored in  a seperate set to ensure that each product has a unique id.

This class has following methods
1. add_item -> will be used to add new product object into the inventory
2. remove_item -> to delete specific product from the inventory based on it's keys
3. update_price,update_quantity, update_price_quantity -> used to update product's price/quantity based on the product id passed to the function
4. list_product -> to print all the available products in the inventory
5. specific_item -> to get name, price and quantity of product in inventory based on it's id
6. low_stock_alert -> to list out products having quantity below the threshold passed in the function
7. total_inventory_value -> to generate report on the total items in the inventory and it's total value
8. save_data -> this function is used to store all the transactions made in the inventory by the user before exiting the program

## main function

Used to allow user to interact with the program using CLI.

All the logic is written in while loop and it extis the loop once user decides to quit.

Following choices are given to user:
1. Add Product
2. Update Product
3. Delete Product
4. View Product
5. List All Products
6. Low-Stock Alert
7. Total Inventory Value
8. Exit

The user will enter the number based on the corresponding operation to be performed 

on entering 8 the user will exit the program


