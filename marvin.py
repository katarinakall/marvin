#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python
Funktioner till Marvin
kakl19
2019-10-03
"""
import random

def say_goodbye():
    """
    Says goodbye to the user.
    """
    print("Bye, bye - and welcome back anytime!")

def say_hello():
    """
    Askes for users name and prints a greeting to the user.
    """
    name = input("What is your name? ")
    print("\nTotoro says:\n")
    print("Hello %s - it is nice to meet you!" % name)

def convert_celcius_to_franeheit():
    """
    Converts temperature from celsius to farenheit.
    """
    celsius = input("What is the temperature in Celsius? ")
    try:
        farenheit = int(celsius) * 9 / 5 + 32
        print(celsius, "degrees Celsius is", farenheit, "degrees Farenheit.")
    except ValueError:
        print("Celsius must be a number.")

def multiply_word():
    """
    Takes a word and prints it as many times as the user wants.
    """
    word_to_multiply = input("What word do you want multiplied? ")
    times = input("How many times do you want Totoro to multiply it? ")
    try:
        times = int(times)
        while times > 0:
            print(word_to_multiply)
            times -= 1

    except ValueError:
        print("The number of times you want to multiply a word have to be a"\
            " number! Totoro could´nt multiply your word. ")

def calculate_mean_and_sum():
    """
    Calcultates the mean and sum of a number of values enterd by the user.
    """
    numbers_enterd = 0
    total_sum = 0
    done = False

    while done is False:
        number = input("Enter a number and press enter. Write 'done' get total"\
                " sum and mean value. ")
        if number == 'done':
            done = True
            print("The total sum of the numbers you enterd is:", total_sum,\
                "and the mean value is", total_sum / numbers_enterd, ".")
        else:
            try:
                number = int(number)
                total_sum += number
                numbers_enterd += 1
            except ValueError:
                print("You didn´t enter a number.")

def compare_numbers():
    """
    Compares two numbers and tells which number is bigger.
    """
    done = False
    first_number = input("Enter the first number you want to compare with ")

    try:
        first_number = int(first_number)
    except ValueError:
        print("You didn´t enter a number.")
        first_number = input("Enter the first number you want to compare with ")
        first_number = int(first_number)

    while done is False:
        number = input("Enter the next number or write 'done' if you want to"\
                        " qo back to the menu. ")
        if number == 'done':
            done = True
        else:
            try:
                number = int(number)
            except ValueError:
                print("You didn´t enter a number.")

            if(number > first_number):
                print("The new number", number, "was bigger than the old number", first_number)
            elif(number < first_number):
                print("The new number", number, "was smaller than the old number", first_number)
            else:
                print("The new number", number, "was the same as than the old number", first_number)

        first_number = number

def write_funny_word():
    """
    Takes a word and writes it by repeting letters.
    """
    word = input("What word do you want to have written in a funny way? ")
    count = 1
    funny_word = ""

    for letter in word:
        for _ in range(count):
            funny_word += letter
        funny_word += '-'
        count += 1
    lenght = len(funny_word) -1
    print(funny_word[:lenght])

def is_isogram():
    """
    Takes a word and controlls if it is an isogram (no letter is used more than once).
    """
    word = input("What word do you want check? ")
    isogram = True

    for char in word:
        count = word.count(char)
        if count > 1:
            isogram = False

    if isogram is True:
        print("Match")
    else:
        print("No match")

def mix_letters():
    """
    Takes a word, mixes the letters and then prints it
    """
    word = input("What word do you want to mix? ")
    lst = list(word)
    random.shuffle(lst)
    print(''.join(lst))

def anagram():
    """
    Takes two strings and sees if they contains the same letters.
    """
    word_one = input("Enter the first word: ")
    word_two = input("Enter the second word: ")

    word_one = sorted(word_one.lower())
    word_two = sorted(word_two.lower())

    if(word_one == word_two):
        print("Match")
    else:
        print("No Match")

def acronym_maker():
    """
    Creates an acronym by combining all uppercase letters to one word.
    """
    acronym_base = input("What words do you want to include in your acronym? ")
    acronym = ''
    for letter in acronym_base:
        if(letter.isupper()):
            acronym += letter

    print(acronym)

def string_masker():
    """
    Replaces all letters in string with '#' exept the four last letters.
    """
    word = input("Which word do you want to mask? ")
    cut = len(word)-4
    rest = word[cut:]
    word = word[:cut]
    result = ""
    for _ in word:
        result += '#'

    print(result + rest)

def generate_nickname():
    """
    Combines two names to a nickname.
    """
    name_one = input("Enter the first namne you want in the nickname: ")
    name_two = input("Enter the second name you want in the nickname: ")
    vowels = 'aeiouy'

    for letter in name_one:
        if letter in vowels:
            index = name_one.find(letter)
            name_one = name_one[:index]
            break

    for letter in name_two:
        if letter in vowels:
            index = name_two.find(letter)
            name_two = name_two[index:]
            break

    print(name_one + name_two)
