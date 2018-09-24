#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Enter three sides of the triangle: ')

a = int(input())
b = int(input())
c = int(input())

if a < 0 or b < 0 or c < 0:
    print('Length of side must be positive!')
    exit(0)

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Yes')
else:
    print('No')

