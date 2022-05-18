#!/usr/bin/env python
import unittest
from main import change

class testchange(unittest.TestCase):
    def test_bas(self):
        testcase = "ada lovelace"
        expected = "lovelace ada"
        self.assertEqual(change(testcase), expected)
    def test_prim(self):
        testcase = ""
        expected = ""
        self.assertEqual(change(testcase), expected)

unittest.main()