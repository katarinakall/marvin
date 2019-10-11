#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Marvin är en chattbot som heter Tototro.
kakl19
2019-10-03
"""
import marvin
import inventory
import quotes
import answer

totoro_image = r"""
                              !         !
                             ! !       ! !
                            ! . !     ! . !
                               ^^^^^^^^^ ^
                             ^             ^
                           ^  (0)       (0)  ^
                          ^        ""         ^
                         ^   ***************    ^
                       ^   *                 *   ^
                      ^   *   /\   /\   /\    *    ^
                     ^   *                     *    ^
                    ^   *   /\   /\   /\   /\   *    ^
                   ^   *                         *    ^
                   ^  *                           *   ^
                   ^  *                           *   ^
                    ^ *                           *  ^
                     ^*                           * ^
                      ^ *                        * ^
                      ^  *                      *  ^
                        ^  *       ) (         * ^
                            ^^^^^^^^ ^^^^^^^^^
"""

def generate_menue():
    """
    Prints menue
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(totoro_image)
    print("Hi, I'm Totoro. What can I do for you?")
    print("1) Tell Totoro what your name is.")
    print("2) Let Totoro convert Celsius to Farenheit.")
    print("3) Let Totoro multiply words.")
    print("4) Enter as many numbers as you want and let Totoro tell you the total sum and mean value. ")
    print("5) Enter a number and let Totoro tell you if the number you enterd was bigger,"\
            " smaller or the same as the previous number. ")
    print("6) Enter a word and Totoro will write it in a funny way. ")
    print("7) Let Totoro check if a word is an isogram. ")
    print("8) Enter a word and let Totoro scramble the letters in it. ")
    print("9) Let Totoro check if two words are anagrams. ")
    print("10) Let Totoro create an acronym for you. ")
    print("11) Let Totoro mask a string. ")
    print("12) Let Totoro tell you how he´s feeling.")
    print("A4) Let Totoro create a combined nickname of two names. ")
    print("You can also type these commands: citat, hej, lunch, inv.")
    print("q) Quit.")

def handle_menue_input():
    """
    Handles menue input.
    """
    choice = input("--> ")

    if choice == "q":
        marvin.say_goodbye()
        quit()

    elif choice == "1":
        marvin.say_hello()

    elif choice == "2":
        marvin.convert_celcius_to_franeheit()

    elif choice == "3":
        marvin.multiply_word()

    elif choice == "4":
        marvin.calculate_mean_and_sum()

    elif choice == "5":
        marvin.compare_numbers()

    elif choice == "6":
        marvin.write_funny_word()

    elif choice == "7":
        marvin.is_isogram()

    elif choice == "8":
        marvin.mix_letters()

    elif choice == "9":
        marvin.anagram()

    elif choice == "10":
        marvin.acronym_maker()

    elif choice == "11":
        marvin.string_masker()

    elif choice == "12":
        answer.date_mood_number()

    elif choice == "A4" or choice == "a4":
        marvin.generate_nickname()

    elif choice == "inv":
        inventory.show_inventory()

    elif choice.startswith("inv pick"):
        item = choice[9:]
        inventory.pick(item)

    elif choice == "inv drop":
        inventory.drop_all()

    elif choice.startswith("inv drop"):
        item = choice[9:]
        inventory.drop(item)

    elif "citat" in choice.lower():
        quotes.give_quote()

    elif "hej" in choice.lower():
        answer.greeting()

    elif "lunch" in choice.lower():
        answer.lunch()

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")


"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
inventory.read_inventory()
while True:
    generate_menue()
    handle_menue_input()
