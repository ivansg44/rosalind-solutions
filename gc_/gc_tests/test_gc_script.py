#!/usr/bin/env python3

import os
import tempfile
import unittest

from gc_ import gc_script


class TestGcScript(unittest.TestCase):
    gc_dir = os.path.dirname(os.path.abspath(__file__))
    test_gc_input = os.path.join(gc_dir, "test_gc_input.txt")

    def test_gc_script(self):
        with tempfile.NamedTemporaryFile() as actual_output_fp:
            gc_script.main(self.test_gc_input, actual_output_fp.name)

            actual_output_id = actual_output_fp.readline()
            actual_output_id = actual_output_id.decode("utf-8")
            actual_output_id = actual_output_id.strip()

            actual_output_percent = actual_output_fp.readline()
            actual_output_percent = actual_output_percent.decode("utf-8")
            actual_output_percent = float(actual_output_percent)

        self.assertEqual("Rosalind_0808", actual_output_id)
        self.assertTrue(60.918540 < actual_output_percent < 60.920540)


if __name__ == "__main__":
    unittest.main()
