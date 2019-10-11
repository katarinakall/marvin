#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Kod för att hantera Marvins citat.
kakl19
2019-10-10
"""
import random

def give_quote():
    """
    Reads quotes from file and returns a random one.
    """
    quoteList = []
    with open("quotes.txt", "r") as filehandler:
        for line in filehandler:
            quoteList.append(line.strip())
    index = random.randint(0, len(quoteList)-1)

    print(quoteList.pop(index))
