#!/usr/bin/env python3
"""test city """
import unittest
import pep8
from models.city import City


class CityTesting(unittest.TestCase):
    """Check City class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_city = 'models/city.py'
        result = pep8style.check_files([path_city])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()