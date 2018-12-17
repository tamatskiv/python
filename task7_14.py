#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def ui_input() -> str:
    """This function takes user E-mail"""
    email = input('Your E-mail: ')
    return email

def is_correct_email(email: str) -> bool:
    """"This function checks user E-mail for correctness"""
    result = True if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$", email) else False
    return result

def ui_output(result: str) -> None:
    """This function prints the result"""
    print(result)

ui_output(is_correct_email(ui_input()))
