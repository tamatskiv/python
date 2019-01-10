#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes number of people"""
    return input('Enter cards numbers(spaces needed): ')

def blackjack_result(cards):
    """Thus function makes a decision about how much card names "A" will have points and returns sum of all cards"""
    sum = 0
    a_cards = 0
    dictionary = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }
    for card in cards.split():
        if card in dictionary:
            sum = sum + dictionary[card]
        elif card == 'A':
            a_cards = a_cards + 1

    if a_cards > 0:
        for i in range(a_cards):
            if a_cards > 1:
                sum = sum + 1
                a_cards = a_cards - 1
            else:
                if sum + 11 < 22:
                    sum = sum + 11
                else:
                    sum = sum + 1

    return sum

def ui_output(result: int) -> None:
    """This function prints the result"""
    if(result<22):
        print(result)
    else:
        print("Bust")

ui_output(blackjack_result(ui_input()))


