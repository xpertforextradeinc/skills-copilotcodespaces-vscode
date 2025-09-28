"""
Test module for forex_api.py

Simple tests to validate the forex API functionality.
"""

import sys
import os
import unittest
from unittest.mock import patch, Mock

# Add the parent directory to the path so we can import forex_api
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import forex_api


class TestForexAPI(unittest.TestCase):
    """Test cases for the forex API functions."""
    
    def test_successful_api_call(self):
        """Test successful API call with valid response."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'USD': 1.1234}
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('forex_api.requests.get', return_value=mock_response):
            result = forex_api.get_eur_usd_price()
            self.assertIsInstance(result, float)
            self.assertEqual(result, 1.1234)
    
    def test_api_timeout(self):
        """Test handling of API timeout."""
        with patch('forex_api.requests.get', side_effect=forex_api.requests.exceptions.Timeout):
            result = forex_api.get_eur_usd_price()
            self.assertIsNone(result)
    
    def test_connection_error(self):
        """Test handling of connection error."""
        with patch('forex_api.requests.get', side_effect=forex_api.requests.exceptions.ConnectionError):
            result = forex_api.get_eur_usd_price()
            self.assertIsNone(result)
    
    def test_invalid_json(self):
        """Test handling of invalid JSON response."""
        mock_response = Mock()
        mock_response.json.side_effect = forex_api.json.JSONDecodeError("Invalid JSON", "", 0)
        mock_response.raise_for_status.return_value = None
        
        with patch('forex_api.requests.get', return_value=mock_response):
            result = forex_api.get_eur_usd_price()
            self.assertIsNone(result)
    
    def test_missing_usd_rate(self):
        """Test handling when USD rate is missing from response."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'GBP': 0.85}  # Missing USD
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('forex_api.requests.get', return_value=mock_response):
            result = forex_api.get_eur_usd_price()
            self.assertIsNone(result)
    
    def test_invalid_rate_value(self):
        """Test handling of invalid rate value."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'USD': 'invalid'}  # Invalid rate value
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('forex_api.requests.get', return_value=mock_response):
            result = forex_api.get_eur_usd_price()
            self.assertIsNone(result)
    
    def test_fallback_function_success(self):
        """Test fallback function when primary API succeeds."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'USD': 1.2345}
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('forex_api.requests.get', return_value=mock_response):
            result = forex_api.get_forex_price_with_fallback()
            self.assertIsInstance(result, float)
            self.assertEqual(result, 1.2345)


if __name__ == '__main__':
    unittest.main()