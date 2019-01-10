#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from task7_1 import offset_str
import unittest


class UnitTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(offset_str("forwhomthebelltolls", 3), "whomthebelltollsfor")

    def test_second(self):
        self.assertEqual(offset_str("verycomplexnumber", -6), "numberverycomplex")


if __name__ == '__main__':
    unittest.main()
