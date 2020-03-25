#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from lcsm import lcsm_script


class TestLcsmScript(unittest.TestCase):
    lcsm_dir = os.path.dirname(os.path.abspath(__file__))
    test_lcsm_input = os.path.join(lcsm_dir, "test_lcsm_input.txt")
    test_lcsm_output = os.path.join(lcsm_dir, "test_lcsm_output.txt")

    def test_lcsm_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            lcsm_script.main(self.test_lcsm_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_lcsm_output, fp.name))

if __name__ == "__main__":
    unittest.main()
