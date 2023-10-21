#!/usr/bin/env python3
"""test review """
import unittest
import pep8
from models.review import Review


class ReviewTesting(unittest.TestCase):
    """Check Review class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_review = 'models/review.py'
        result = pep8style.check_files([path_review])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()