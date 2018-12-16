#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes user word(s)"""
    return input('Your word(s): ')

def count_vowels(word: str) -> int:
    """"This function counts vowels in the word(s)"""
    number = 0
    letters = ['a', 'o', 'u', 'i', 'e', 'y']
    for letter in word:
        if letter in letters:
            number += 1
    return number

def ui_output(word: str) -> None:
    """This function prints the number of vowels"""
    print('Number of vowels = ', word)

ui_output(count_vowels(ui_input()))


