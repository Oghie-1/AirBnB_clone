#!/usr/bin/env python3
"""test amenity  """
import unittest
import pep8
from models.amenity import Amenity


class AmenityTesting(unittest.TestCase):
    """Check Amenity class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()