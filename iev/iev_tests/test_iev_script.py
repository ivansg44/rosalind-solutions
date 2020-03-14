#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from iev import iev_script


class TestIevScript(unittest.TestCase):
    iev_dir = os.path.dirname(os.path.abspath(__file__))
    test_iev_input = os.path.join(iev_dir, "test_iev_input.txt")
    test_iev_output = os.path.join(iev_dir, "test_iev_output.txt")

    def test_iev_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            iev_script.main(self.test_iev_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_iev_output, fp.name))


if __name__ == "__main__":
    unittest.main()
