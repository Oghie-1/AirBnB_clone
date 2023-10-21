#!/usr/bin/env python3
"""test User """
import unittest
import pep8
from models.user import User


class UserTesting(unittest.TestCase):
    """Check User class"""

    def test_pep8(self):
        """Test PEP 8 compliance."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pep8style.check_files([path_user])
        self.assertEqual(
            result.total_errors, 0,
            "Found PEP 8 style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()