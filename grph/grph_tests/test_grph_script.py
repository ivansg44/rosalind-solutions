#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from grph import grph_script


class TestGrphScript(unittest.TestCase):
    grph_dir = os.path.dirname(os.path.abspath(__file__))
    test_grph_input = os.path.join(grph_dir, "test_grph_input.txt")
    test_grph_output = os.path.join(grph_dir, "test_grph_output.txt")

    def test_grph_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            grph_script.main(self.test_grph_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_grph_output, fp.name))


if __name__ == "__main__":
    unittest.main()
