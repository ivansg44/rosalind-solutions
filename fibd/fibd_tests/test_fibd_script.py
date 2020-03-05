#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from fibd import fibd_script


class TestFibdScript(unittest.TestCase):
    fibd_dir = os.path.dirname(os.path.abspath(__file__))
    test_fibd_input = os.path.join(fibd_dir, "test_fibd_input.txt")
    test_fibd_output = os.path.join(fibd_dir, "test_fibd_output.txt")

    def test_fibd_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            fibd_script.main(self.test_fibd_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_fibd_output, fp.name))


if __name__ == "__main__":
    unittest.main()
