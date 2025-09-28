"""
Forex Trading API Module

This module provides functionality to fetch live EUR/USD exchange rates
from a forex trading API with proper error handling.
"""

import requests
import json
from typing import Optional


def get_eur_usd_price() -> Optional[float]:
    """
    Fetch live EUR/USD exchange rate from a forex API.
    
    Returns:
        float: The EUR/USD exchange rate as a float, or None if an error occurs
        
    Raises:
        None: All exceptions are handled gracefully and logged
    """
    # Using exchangerate-api.com free tier (no API key required for basic usage)
    api_url = "https://api.exchangerate-api.com/v4/latest/EUR"
    
    try:
        # Make HTTP request with timeout
        response = requests.get(api_url, timeout=10)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract USD rate from the response
        if 'rates' in data and 'USD' in data['rates']:
            usd_rate = data['rates']['USD']
            
            # Validate that the rate is a number
            if isinstance(usd_rate, (int, float)) and usd_rate > 0:
                return float(usd_rate)
            else:
                print(f"Error: Invalid USD rate received: {usd_rate}")
                return None
        else:
            print("Error: USD rate not found in API response")
            return None
            
    except requests.exceptions.Timeout:
        print("Error: API request timed out")
        return None
        
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to forex API")
        return None
        
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred: {e}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed: {e}")
        return None
        
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response from API")
        return None
        
    except KeyError as e:
        print(f"Error: Missing expected field in API response: {e}")
        return None
        
    except Exception as e:
        print(f"Error: Unexpected error occurred: {e}")
        return None


def get_forex_price_with_fallback() -> Optional[float]:
    """
    Get EUR/USD price with fallback to alternative API if primary fails.
    
    Returns:
        float: The EUR/USD exchange rate, or None if all APIs fail
    """
    # Try primary API first
    price = get_eur_usd_price()
    if price is not None:
        return price
    
    # Fallback to alternative free API
    try:
        fallback_url = "https://open.er-api.com/v6/latest/EUR"
        response = requests.get(fallback_url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if 'rates' in data and 'USD' in data['rates']:
            usd_rate = data['rates']['USD']
            if isinstance(usd_rate, (int, float)) and usd_rate > 0:
                return float(usd_rate)
                
    except Exception as e:
        print(f"Fallback API also failed: {e}")
    
    return None


if __name__ == "__main__":
    # Test the function
    print("Fetching EUR/USD exchange rate...")
    rate = get_eur_usd_price()
    
    if rate is not None:
        print(f"EUR/USD: {rate:.4f}")
    else:
        print("Failed to fetch exchange rate")
        
    # Test fallback function
    print("\nTesting fallback function...")
    fallback_rate = get_forex_price_with_fallback()
    if fallback_rate is not None:
        print(f"EUR/USD (with fallback): {fallback_rate:.4f}")
    else:
        print("All APIs failed")