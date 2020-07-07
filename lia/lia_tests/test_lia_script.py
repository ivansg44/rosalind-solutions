#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from lia import lia_script


class TestLiaScript(unittest.TestCase):
    lia_dir = os.path.dirname(os.path.abspath(__file__))
    test_lia_input = os.path.join(lia_dir, "test_lia_input.txt")
    test_lia_output = os.path.join(lia_dir, "test_lia_output.txt")

    def test_lia_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            lia_script.main(self.test_lia_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_lia_output, fp.name))


if __name__ == "__main__":
    unittest.main()
