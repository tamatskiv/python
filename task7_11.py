#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import collections

def ui_input() -> str:
    """This function takes user string"""
    string = input('Your string: ')
    return string

def sort_from_smallest(string: str) -> str:
    """This function sorts word in ascending order of letters"""
    words = re.sub("[^\w]", " ", string).split()
    list = dict()
    for word in words:
        if len(word) in list:
            list[len(word)] = list[len(word)] + " " + word
        else:
            list[len(word)] = word
    list = collections.OrderedDict(sorted(list.items()))
    result = " ".join(list.values())
    return result

def ui_output(result: str) -> None:
    """This function prints the result"""
    print(result)

ui_output(sort_from_smallest(ui_input()))