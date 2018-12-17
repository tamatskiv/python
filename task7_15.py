#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string

def generate_password() -> str:
    """"This function generates password for user"""
    letters = [random.choice(string.ascii_letters) for _ in range(8)]
    numbers = random.choice(string.digits)
    symbols = random.choice(string.punctuation)
    password = letters + list(numbers) + list(symbols)
    random.shuffle(password)
    result_password = ''.join(password)
    return result_password

def ui_output(result_pswd: str) -> None:
    """This function prints generated password"""
    print('Your password: ', result_pswd)

ui_output(generate_password())
