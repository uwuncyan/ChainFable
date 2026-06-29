# test_chainfable.py
"""
Tests for ChainFable module.
"""

import unittest
from chainfable import ChainFable

class TestChainFable(unittest.TestCase):
    """Test cases for ChainFable class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainFable()
        self.assertIsInstance(instance, ChainFable)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainFable()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
