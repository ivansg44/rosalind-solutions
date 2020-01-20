#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from subs import subs_script


class TestSubsScript(unittest.TestCase):
    subs_dir = os.path.dirname(os.path.abspath(__file__))
    test_subs_input = os.path.join(subs_dir, "test_subs_input.txt")
    test_subs_output = os.path.join(subs_dir, "test_subs_output.txt")

    def test_subs_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            subs_script.main(self.test_subs_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_subs_output, fp.name))


if __name__ == "__main__":
    unittest.main()
