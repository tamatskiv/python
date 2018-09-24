#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Enter three sides of the triangle: ')

a = int(input())
b = int(input())
c = int(input())

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Yes')
else:
    print('No')

