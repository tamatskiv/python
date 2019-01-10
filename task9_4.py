#!/usr/bin/env python3
#-*- coding: utf-8 -*-

arabic = int(input("Enter arabic number: "))
roman = str(input("Enter roman number: "))


def toRomanNumerals(arabicNumeral):
    """This function transforms arabic numerals to roman"""
    if arabicNumeral > 3999:
        raise Exception('Number can not be greater than 3999')

    digitsSymbols = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dozensSymbols = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundredsSymbols = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousandsSymbols = ["", "M", "MM", "MMM"]

    thousands = thousandsSymbols[arabicNumeral // 1000]
    hundreds = hundredsSymbols[arabicNumeral // 100 % 10]
    dozens = dozensSymbols[arabicNumeral // 10 % 10]
    digits = digitsSymbols[arabicNumeral % 10]

    return thousands + hundreds + dozens + digits

def toArabicNumerals(romanNumeral):
    """This function transforms roman numerals to arabic"""
    romanNumeral = romanNumeral.upper()

    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    arabicNumeral = 0

    count = len(romanNumeral)
    for i in range(count):
        if i < count - 1 and dictionary[romanNumeral[i]] < dictionary[romanNumeral[i + 1]]:
            continue
        elif i > 0 and dictionary[romanNumeral[i - 1]] < dictionary[romanNumeral[i]]:
            arabicNumeral += dictionary[romanNumeral[i]] - dictionary[romanNumeral[i - 1]]
        else:
            arabicNumeral += dictionary[romanNumeral[i]]

    return arabicNumeral


print('{} = {}'.format(arabic, toRomanNumerals(arabic)))
print('{} = {}'.format(roman, toArabicNumerals(roman)))
