#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from fib import fib_script


class TestFibScript(unittest.TestCase):
    fib_dir = os.path.dirname(os.path.abspath(__file__))
    test_fib_input = os.path.join(fib_dir, "test_fib_input.txt")
    test_fib_output = os.path.join(fib_dir, "test_fib_output.txt")

    def test_fib_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            fib_script.main(self.test_fib_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_fib_output, fp.name))


if __name__ == "__main__":
    unittest.main()
