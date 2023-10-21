#!/usr/bin/env python3
"""test state """
import unittest
import pep8
from models.state import State


class StateTesting(unittest.TestCase):
    """Check State class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_state = 'models/state.py'
        result = pep8style.check_files([path_state])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()