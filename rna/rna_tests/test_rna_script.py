#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from rna import rna_script


class TestRnaScript(unittest.TestCase):
    rna_dir = os.path.dirname(os.path.abspath(__file__))
    test_rna_input = os.path.join(rna_dir, "test_rna_input.txt")
    test_rna_output = os.path.join(rna_dir, "test_rna_output.txt")

    def test_rna_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            rna_script.main(self.test_rna_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_rna_output, fp.name))


if __name__ == "__main__":
    unittest.main()
