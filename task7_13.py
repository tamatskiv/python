#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input_1() -> str:
    """This function takes first user string"""
    string1 = input('Your first string: ')
    return string1

def ui_input_2() -> str:
    """This function takes second user string"""
    string2 = input('Your second string: ')
    return string2

def checker(string1: str, string2: str) -> bool:
    """This function checks whether the set is contained in the first string"""
    result = set(string1).issubset(set(string2))
    return result

def ui_output(result: bool) -> None:
    print(result)

ui_output(checker(ui_input_1(), ui_input_2()))
