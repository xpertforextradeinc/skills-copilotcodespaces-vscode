#!/usr/bin/env python3
"""
Example usage of the forex API module.

This script demonstrates how to use the forex API functions to fetch EUR/USD rates.
"""

from forex_api import get_eur_usd_price, get_forex_price_with_fallback
import time


def main():
    """Main function to demonstrate forex API usage."""
    print("=== Forex Trading API Example ===\n")
    
    # Example 1: Basic usage
    print("1. Fetching EUR/USD rate using primary function:")
    rate = get_eur_usd_price()
    
    if rate is not None:
        print(f"   Success! EUR/USD: {rate:.4f}")
        print(f"   This means 1 EUR = {rate:.4f} USD")
    else:
        print("   Failed to fetch rate from primary API")
    
    print()
    
    # Example 2: Using fallback function
    print("2. Fetching EUR/USD rate with fallback support:")
    fallback_rate = get_forex_price_with_fallback()
    
    if fallback_rate is not None:
        print(f"   Success! EUR/USD: {fallback_rate:.4f}")
        
        # Calculate conversion examples
        eur_amounts = [100, 500, 1000]
        print(f"   Conversion examples:")
        for eur in eur_amounts:
            usd = eur * fallback_rate
            print(f"   {eur} EUR = {usd:.2f} USD")
    else:
        print("   Failed to fetch rate from all APIs")
    
    print()
    
    # Example 3: Error handling demonstration
    print("3. Error handling is built-in - no exceptions are raised")
    print("   The function returns None when errors occur and logs the issue")
    
    print(f"\nExample complete!")


if __name__ == "__main__":
    main()