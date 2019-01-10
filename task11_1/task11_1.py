#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse(file: str) -> int:
    """This function parces file with "split" """
    f = open(file, 'r')
    for line in f:
        bytes = line.split()[9]
        yield int(bytes)

def count(bytes: list) -> int:
    """This function counts size of bytes"""
    size = 0
    for byte in bytes:
        size += byte
    return size

def ui_output(result: int) -> None:
    """This function prints the result"""
    print('Size =' , result)

ui_output(count(parse('2017_05_07_nginx.txt')))