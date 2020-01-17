#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from hamm import hamm_script


class TestHammScript(unittest.TestCase):
    hamm_dir = os.path.dirname(os.path.abspath(__file__))
    test_hamm_input = os.path.join(hamm_dir, "test_hamm_input.txt")
    test_hamm_output = os.path.join(hamm_dir, "test_hamm_output.txt")

    def test_hamm_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            hamm_script.main(self.test_hamm_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_hamm_output, fp.name))


if __name__ == "__main__":
    unittest.main()
