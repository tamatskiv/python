#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import math
import timeit

def power_by_shift() -> int:
    return 2 << 63

def power_by_operator() -> int:
    return 2 ** 64

def power_by_pow() -> int:
    return pow(2, 64)

def power_by_math_pow() -> float:
    return math.pow(2, 64)

def revers_by_map(strings: list) -> list:
    return list(map(lambda x: x[::-1], strings))

def revers_by_comprehension(strings: list) -> list:
    result = []
    result += [string[::-1] for string in strings]
    return result

def revers_by_for(strings: list) -> list:
    result = []
    for string in strings:
        string = string[::-1]
        result.append(string)
    return result

def timeit_map() -> float:
    return timeit.timeit('revers_by_map', \
                         setup='from __main__ import revers_by_map; \
                         strings = [ \
                        "lorem", "ipsum", "text", "for", "python", "123456", \
                        "lorem", "ipsum", "text", "for", "python", "123456", \
                        "lorem", "ipsum", "text", "for", "python", "123456", \
                        ]', \
                         number = 10000)

def timeit_comprehension() -> float:
    return timeit.timeit('revers_by_comprehension', \
                         setup='from __main__ import revers_by_comprehension; \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         ]', \
                         number=10000)

def timeit_for_loop() -> float:
    return timeit.timeit('revers_by_for', \
                         setup='from __main__ import revers_by_for; \
                         strings = [ \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         "lorem", "ipsum", "text", "for", "python", "123456", \
                         ]', \
                         number=10000)

def ui_output(map_time: float, comp_time: float, for_time: float,) -> None:
    print("Map() time is", map_time)
    print("Comprehension time is", comp_time)
    print("For time is", for_time)

ui_output(timeit_map(), timeit_comprehension(), timeit_for_loop())