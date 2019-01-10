#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

amount = input("Enter amount of money with dot): ")


def num_to_words(amount):
    """"This function returns amount of money in words"""
    digits = {
        0: 'нуль', 1: 'одна',
        2: 'дві',  3: 'три',
        4: 'чотири', 5: 'п\'ять',
        6: 'шість', 7: 'сім',
        8: 'вісім', 9: 'дев\'ять',
        10: 'десять',  11: 'одинадцять',
        12: 'дванадцять', 13: 'тринадцять',
        14: 'чотирнадцять', 15: 'п\'ятнадцять',
        16: 'шістнадцять', 17: 'сімнадцять',
        18: 'вісімнадцять', 19: 'дев\'ятнадцять'
    }

    dozens = {
        2: 'двадцять', 3: 'тридцять',
        4: 'сорок', 5: 'п\'ятдесят',
        6: 'шістдесят', 7: 'сімдесят',
        8: 'вісімдесят', 9: 'дев\'яносто'
    }

    hundreds = {
        1: 'сто', 2: 'двісті',
        3: 'триста', 4: 'чотириста',
        5: 'п\'ятсот', 6: 'шістсот',
        7: 'сімсот', 8: 'вісімсот',
        9: 'дев\'ятсот'
    }

    strnumber = str(amount)
    if amount < 20:
        return digits[amount]
    elif amount < 100:
        if strnumber[-1] == '0':
            return dozens[int(strnumber[0])]
        else:
            return dozens[int(strnumber[0])] + " " + num_to_words(int(strnumber[1]))
    else:
        if strnumber[1:3] == '00':
            return hundreds[int(strnumber[0])]
        else:
            return hundreds[int(strnumber[0])] + " " + num_to_words(int(strnumber[1:3]))

def split_by_thousands(amount):
    array = amount.split('.')
    if len(array[1]) == 1:
        array[1] = array[1] + '0'
    kopecks = int(array[1])
    hryvnias = int(array[0])
    array_thousands = []
    array_thousands.append(kopecks)
    while hryvnias != 0:
        array_thousands.append(int(hryvnias % 1000))
        hryvnias = int(hryvnias/1000)
    return array_thousands

def main(amount):

    names_of_numbers = {
        0: ['копійка', 'копійки', 'копійок'],
        1: ['гривня', 'гривні', 'гривень'],
        2: ['тисяча', 'тисячі', 'тисяч'],
        3: ['мільйон', 'мільйони', 'мільйонів'],
        4: ['мільярд', 'мільярди', 'мільярдів'],
    }

    arr = split_by_thousands(amount)
    result = ''

    for i in reversed(range(len(arr))):
        result = result + " " + num_to_words(arr[i])
        strnum = str(arr[i])

        while len(strnum) < 3:
            strnum = '0' + strnum

        if re.match(r'.[^1]1', strnum):
            result = result + " " + names_of_numbers[i][0]
        elif re.match(r'.[^1][234]', strnum):
            result = result + " " + names_of_numbers[i][1]
        else:
            result = result + " " + names_of_numbers[i][2]
    return result.strip()

print(main(amount))