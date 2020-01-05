#!/usr/bin/env python3

import filecmp
import os
import tempfile
import unittest

from revc import revc_script


class TestRevcScript(unittest.TestCase):
    revc_dir = os.path.dirname(os.path.abspath(__file__))
    test_revc_input = os.path.join(revc_dir, "test_revc_input.txt")
    test_revc_output = os.path.join(revc_dir, "test_revc_output.txt")

    def test_revc_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            revc_script.main(self.test_revc_input, fp.name)
            self.assertTrue(filecmp.cmp(self.test_revc_output, fp.name))


if __name__ == "__main__":
    unittest.main()
