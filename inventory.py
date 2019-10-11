#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Kod för att hantera Marvins inventarie.
kakl19
2019-10-03
"""

def read_inventory():
    """
    Loads inventory content from file.
    """
    with open("inv.data", "r") as file:
        content = file.read()
    return content



def show_inventory():
    """
    Prints all items int the inventory.
    """
    content = read_inventory()
    if (len(content) is 0):
        print("Your inventory is empty.")
    else:
        print("You have " + str(len(content.split())) + " item(s) in your inventory.")
    print("Inventory: ")
    print(content)



def pick(item):
    """
    Takes one item and adds it to the inventory.
    """
    content = read_inventory()

    with open("inv.data", "a") as file:
        if(len(content.split()) == 4):
            print("Inventory is full")
        elif(len(content.split()) >= 1):
            file.write(" " + item + " ")
            print("You have picked up: " + item)
        else:
            file.write(item + " ")
            print("You have picked up: " + item)



def drop(item):
    """
    Removes an item from the inventory.
    """
    content = read_inventory()

    if item in content: # check if item to remove exists
        if content.index(item) == 0: # if the item is the first line in the file
            modified_content = content.replace(item, "")
        else:
            modified_content = content.replace(" " + item, "")

        with open("inv.data", "w") as file:
            file.write(modified_content.strip())
        print("You have droped: " + item)
    else:
        print("You don´t have " + item + " in your inventory.")


def drop_all():
    """
    Removes all items from inventory.
    """
    with open("inv.data", "w") as file:
        file.write("")
    print("You droped all your things.")
