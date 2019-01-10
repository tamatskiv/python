#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_random(seed = 654321):
    while True:
        x = str(seed)
        if len(x)!=6:
             x = (6 - len(x)) * '0' + x
        y = x[3:6] + x[0:3]
        result = str(int(x) * int(y))
        if len(result)!=12:
             result = (12 - len(result)) * '0' + result
        seed = result[3:9]
        yield int(seed)

a = my_random()
for i in range(16):
    print(a.__next__())
