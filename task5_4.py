#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import cmath

print('Input a, b, c: ')

a = float(input())
b = float(input())
c = float(input())

if a != 0 and b != 0 and c != 0:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2*a
        print('Result: ', x1, x2)
    elif D == 0:
        x = -b / 2*a
        print('Result: ', x)
    else:
        x1 = complex((-b + cmath.sqrt(D)) / 2*a)
        x2 = complex((-b - cmath.sqrt(D)) / 2*a)
        print('Result: ', x1, x2)
elif a == 0 and b == 0 and c == 0:
    print('Result: x є R')
elif a == 0 and b == 0 and c != 0:
    print('No result')
elif a == 0 and b != 0 and c != 0:
    x = -c / b
    print('Result: ', x)
elif a != 0 and b != 0 and c == 0:
    x1 = 0
    x2 = -b / a
    print('Result: ', x1, x2)
elif (a == 0 and b != 0 and c == 0) or (a != 0 and b == 0 and c == 0):
    print('Result: x = 0')
else:
    if (a > 0 and c > 0) or (a < 0 and c < 0):
        x1 = complex(-cmath.sqrt(-c/a))
        x2 = complex(cmath.sqrt(-c/a))
    else:
        x1 = -math.sqrt(-c/a)
        x2 = math.sqrt(-c/a)
    print('Result: ', x1, x2)