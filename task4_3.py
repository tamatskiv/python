#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import decimal

salary = decimal.Decimal(input('Enter your monthly salary: '))

taxes = salary * decimal.Decimal('0.18')
military_duties = salary * decimal.Decimal('0.015')
all_taxes = decimal.Decimal(taxes) + decimal.Decimal(military_duties)

print('Taxes = ', taxes, 'Military duty = ', military_duties)
print('All taxes = ', all_taxes)
