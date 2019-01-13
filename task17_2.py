#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import math
import timeit

def power_shift() -> int:
    return 2 << 63

def power_operator() -> int:
    return 2 ** 64

def power_pow() -> int:
    return pow(2, 64)

def power_math_pow() -> float:
    return math.pow(2, 64)

def reverse_map(strings: list) -> list:
    return list(map(lambda x: x[::-1], strings))

def reverse_comprehension(strings: list) -> list:
    result = []
    result += [string[::-1] for string in strings]
    return result

def reverse_for(strings: list) -> list:
    result = []
    for string in strings:
        string = string[::-1]
        result.append(string)
    return result

def timeit_shift() -> float:
    return timeit.timeit('power_shift()', \
           setup = "from __main__ import power_shift", \
           number = 5000)

def timeit_operator() -> float:
    return timeit.timeit('power_operator()', \
           setup = "from __main__ import power_operator", \
           number = 5000)

def timeit_pow() -> float:
    return timeit.timeit('power_pow()', \
           setup = "from __main__ import power_pow", \
           number = 5000)

def timeit_math_pow() -> float:
    return timeit.timeit('power_math_pow()', \
           setup = "from __main__ import power_math_pow", \
           number = 5000)

def timeit_map() -> float:
    return timeit.timeit('reverse_map(strings)', \
        setup = 'from __main__ import reverse_map; \
	strings = [ \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	]', \
        number = 5000)

def timeit_comprehension() -> float:
    return timeit.timeit('reverse_comprehension(strings)', \
        setup = 'from __main__ import reverse_comprehension; \
	strings = [ \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	]', \
        number = 5000)

def timeit_for_loop() -> float:
    return timeit.timeit('reverse_for(strings)', \
        setup = 'from __main__ import reverse_for; \
	strings = [ \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	"lorem", "ipsum", "text", "for", "python", "123456", \
        	]', \
        number = 5000)

def ui_output(shift_time: float, operator_time: float, pow_time: float, \
              math_pow_time: float, map_time: float, compreh_time: float, \
              for_time: float,) -> None:
    print("Shift time: ", shift_time)
    print("Time of ** operator: ", operator_time)
    print("Time of pow(): ", pow_time)
    print("Time of Math.pow(): ", math_pow_time)
    print("Time of map(): ", map_time)
    print("Comprehension time: ", compreh_time)
    print("Time of for: ", for_time)

ui_output(timeit_shift(), timeit_operator(), timeit_pow(), \
          timeit_math_pow(), timeit_map(), timeit_comprehension(), \
          timeit_for_loop())