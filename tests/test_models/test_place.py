#!/usr/bin/env python3
"""test place """
import unittest
import pep8
from models.place import Place


class PlaceTesting(unittest.TestCase):
    """Check Place class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_place = 'models/place.py'
        result = pep8style.check_files([path_place])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()