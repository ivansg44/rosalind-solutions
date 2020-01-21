#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from cons import cons_script


class TestConsScript(unittest.TestCase):
    cons_dir = os.path.dirname(os.path.abspath(__file__))
    test_cons_input = os.path.join(cons_dir, "test_cons_input.txt")
    test_cons_output = os.path.join(cons_dir, "test_cons_output.txt")

    def test_cons_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            cons_script.main(self.test_cons_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_cons_output, fp.name))


if __name__ == "__main__":
    unittest.main()
