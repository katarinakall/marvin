#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Kod för att svara på frågor.
kakl19
2019-10-10
"""
import random
import time

lunchQuote = ['Ska vi ta %s?',\
'Ska vi dra ned till %s?',\
'Jag tänkte käka på %s, ska du med?',\
'På %s är det mysigt, ska vi ta där?']

lunchStan = ['Olles krovbar',\
'Lila thai stället',\
'donken',\
'Tex mex stället vid Subway',\
'Subway',\
'Nya Peking',\
'Kebab house',\
'Royal thai',\
'thai stället vid hemmakväll',\
'Gelato',\
'Indian garden',\
'Sumo sushi',\
'Pasterian i stan',\
'Biobaren',\
'Michelangelo']


def greeting():
    """
    Prints a random greeting from a list.
    """
    hello = ['Hej själv! ', 'Trevligt att du bryr dig om mig. ',\
    'Det var länge sedan någon var trevlig mot mig. ', 'Halloj, det ser ut att bli mulet idag. ']
    index = random.randint(0, len(hello)-1)
    print(hello.pop(index))

def lunch():
    """
    Generates where to eat.
    """
    quote = lunchQuote[random.randint(0, len(lunchQuote) - 1)]
    msg = ''
    msg = quote % lunchStan[random.randint(0, len(lunchStan) -1)]
    print(msg)

def date_mood_number():
    """
    Reeds answer from file and adds variables to it.
    """
    date = time.strftime("%c")
    procent = 99.999
    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)
    fucks = 0

    with open("answer.txt", "r") as filehandler:
        file = filehandler.read()

    print(file.format(date=date, procent=procent, mood=mood, fucks=fucks))
