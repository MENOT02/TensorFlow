# test_tensorflowx.py
"""
Tests for TensorFlowX module.
"""

import unittest
from tensorflowx import TensorFlowX

class TestTensorFlowX(unittest.TestCase):
    """Test cases for TensorFlowX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TensorFlowX()
        self.assertIsInstance(instance, TensorFlowX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TensorFlowX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
