#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes number of people"""
    return input('Enter sentence that needs to be converted: ')

def morse_converter(sentence):

    morse_codes = {
        'a': '·−',
        'b': '−···',
        'c': '−·−·',
        'd': '−··',
        'e': '·',
        'f': '··−·',
        'g': '−−·',
        'h': '····',
        'i': '..',
        'j': '·−−−',
        'k': '−·−',
        'l': '·−··',
        'm': '−−',
        'n': '−·',
        'o': '−−−',
        'p': '·−−·',
        'q': '−−·−',
        'r': '·−·',
        's': '···',
        't': '−',
        'u': '··−',
        'v': '···−',
        'w': '·−−',
        'x': '−··−',
        'y': '−·−−',
        'z': '−−··',

        '0': '−−−−−',
        '1': '·−−−−',
        '2': '··−−−',
        '3': '···−−',
        '4': '····−',
        '5': '·····',
        '6': '−····',
        '7': '−−···',
        '8': '−−−··',
        '9': '−−−−·',
        ' ': ' '
    }

    data = sentence.lower()

    signal = ''
    for char in data:
        signal = signal + morse_codes[char]
    return signal

def ui_output(result: str) -> None:
    """This function prints the result"""
    print(result)

ui_output(morse_converter(ui_input()))


