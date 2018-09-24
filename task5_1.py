#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input ('Enter your number: '))

if a & (a - 1):
    print("no")
else:
    print("yes")
