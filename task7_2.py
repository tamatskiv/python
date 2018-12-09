#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def ui_input() -> str:
    """This function takes user string"""
    string = input('Enter your string: ')
    return string

def is_palindrome(string: str) -> bool:
    """This function checks whether is string palindrome"""
    string = re.sub(r'\W+', '', string).lower()
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

def ui_output(result: bool) -> None:
    """Thus function prints the result"""
    print(result)

ui_output(is_palindrome(ui_input()))
