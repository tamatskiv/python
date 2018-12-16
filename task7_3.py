#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string


def ui_input() -> str:
    """This function asks and then takes user sting"""
    string = input("What's your string? \n  ")
    return string

def is_valid(string: str) -> bool:
    OPEN_BRACKETS = {"{", "[", "("}
    CLOSE_BRACKETS = {"]", "}", ")"}
    BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}
    stack = []
    for bracket in string:
        if bracket in OPEN_BRACKETS:
            stack.append(bracket)
        elif bracket in CLOSE_BRACKETS:
            if not stack: return False
            last = stack.pop()
            if BRACKETS_MAP.get(bracket) != last:
                return False

    return not stack

def ui_output(string: str) -> None:
    """This function prints the result"""
    print ("Result = ", string)

ui_output(is_valid(ui_input()))
