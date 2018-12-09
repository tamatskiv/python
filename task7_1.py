#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def offset_str(string: str, offset: int) -> str:
    """This function does the offset of the string""" 
    result_string = string[offset:] + string[:offset]
    return result_string

def ui_output(result: str) -> None:
    """This function prints an offsetted string"""
    print(result)

ui_output(offset_str(input('Your string: '),\
    int(input('The offset: '))))
