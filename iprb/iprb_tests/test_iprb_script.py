#!/usr/bin/env python3

import os
import tempfile
import unittest

from iprb import iprb_script


class TestIprbScript(unittest.TestCase):
    iprb_dir = os.path.dirname(os.path.abspath(__file__))
    test_iprb_input = os.path.join(iprb_dir, "test_iprb_input.txt")

    def test_iprb_script(self):
        with tempfile.NamedTemporaryFile() as fp:
            iprb_script.main(self.test_iprb_input, fp.name)
            actual_output = float(fp.read().strip())
            self.assertTrue(0.78233 < actual_output < 0.78433)


if __name__ == "__main__":
    unittest.main()
