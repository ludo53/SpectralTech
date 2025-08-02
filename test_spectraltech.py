# test_spectraltech.py
"""
Tests for SpectralTech module.
"""

import unittest
from spectraltech import SpectralTech

class TestSpectralTech(unittest.TestCase):
    """Test cases for SpectralTech class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpectralTech()
        self.assertIsInstance(instance, SpectralTech)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpectralTech()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
