#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from dna import dna_script


class TestDnaScript(unittest.TestCase):
    dna_dir = os.path.dirname(os.path.abspath(__file__))
    test_dna_input = os.path.join(dna_dir, "test_dna_input.txt")
    test_dna_output = os.path.join(dna_dir, "test_dna_output.txt")

    def test_dna_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            dna_script.main(self.test_dna_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_dna_output, fp.name))


if __name__ == "__main__":
    unittest.main()
