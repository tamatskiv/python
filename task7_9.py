#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes number of ticket from user"""
    ticket_num = input('Your ticket number: ')
    return ticket_num

def ticket_is_lucky(ticket_num: str) -> str:
    """"This function checks whether number is lucky (split into two parts and checks whether their sum is equal)"""
    if not ticket_num.isdigit(): return False
    first = ticket_num[:len(ticket_num) // 2]
    second = ticket_num[-(len(ticket_num) // 2):]
    result = sum(int(x) for x in first) == sum(int(x) for x in second)
    return result

def ui_output(result: str) -> None:
    """This function print the result"""
    print(result)

ui_output(ticket_is_lucky(ui_input()))