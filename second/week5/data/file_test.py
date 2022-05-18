#!/usr/bin/env python

import unittest
from file import save_file, check_pattern

class TestFile(unittest.TestCase):

    def test_open_file(self):
        case = "file.csv"
        expected = ()
        self.assertTupleEqual(save_file(case), )


if __name__ == '__main__':
    unittest.main()