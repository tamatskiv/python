#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def ui_input() -> str:
    """This function takes user string"""
    string = input('Your string: ')
    return string

def space_remover(string: str) -> str:
    """This function finds extra space and removes them"""
    result = re.sub('( )( )+', r'\1', string).strip()
    return result

def ui_output(result: str) -> None:
    """This function prints the result"""
    print(result)

ui_output(space_remover(ui_input()))