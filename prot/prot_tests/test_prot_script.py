#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from prot import prot_script


class TestProtScript(unittest.TestCase):
    prot_dir = os.path.dirname(os.path.abspath(__file__))
    test_prot_input = os.path.join(prot_dir, "test_prot_input.txt")
    test_prot_output = os.path.join(prot_dir, "test_prot_output.txt")

    def test_prot_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            prot_script.main(self.test_prot_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_prot_output, fp.name))


if __name__ == "__main__":
    unittest.main()
