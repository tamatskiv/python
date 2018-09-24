#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Enter the height and the width of the rectangular door:')

h = int(input())
w = int(input())

print ('Enter three dimensions of the box:')

a = int(input())
b = int(input())
c = int(input())

if a <= h and b <= w:
    print('yes')
elif b <= h and a <= w:
    print('yes')
elif a <= h and c <= w:
    print('yes')
elif c <= h and a <= w:
    print('yes')
elif b <= h and a <= w:
    print('yes')
elif a <= h and c <= w:
    print('yes')
else:
    print('no')
