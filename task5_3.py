#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

player = int(input('Enter the number from 1 to 3 (1 - scissors, 2 - paper, 3 - rock): '))
if player > 3 or player < 1:
    print('Wrong number!')
    exit(0)
comp = random.randint(1,3)

print("Player's choice - ", player, "," , "choice of computer - ", comp)

if player == comp:
    print('Draw')
elif player == 1 and  comp == 2:
    print('Winner: player')
elif player == 2 and comp == 3:
    print('Winner: player')
elif player == 3 and comp == 1:
    print ('Winner: player')
else:
    print('Winner: computer')
