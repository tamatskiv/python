#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input_number() -> int:
    """This function takes number of people"""
    return int(input('Enter number of people: '))

def ui_input_step() -> int:
    """This function takes step"""
    return int(input('Enter step: '))

def ident_survived(number_of_people: int, step: int) -> list:
    """This function identifies person who will survive"""
    people = list(range(1, number_of_people + 1))
    position = 0
    while len(people) > 1:
        position += 1
        person = people.pop(0)
        if position != step:
            people.append(person)
        else:
            position = 0
    return people

def ui_output(survived: list) -> None:
    """This function prints number of survived people"""
    print('Survived: ', survived)

ui_output(ident_survived(ui_input_number(), ui_input_step()))
