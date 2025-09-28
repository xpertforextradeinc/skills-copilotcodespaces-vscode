# Forex Trading API

A Python module that connects to forex trading APIs to fetch live EUR/USD exchange rates with robust error handling.

## Features

- Fetches live EUR/USD exchange rates from free forex APIs
- Comprehensive error handling for network issues, API failures, and invalid data
- Fallback API support for increased reliability
- Returns exchange rate as a float value
- No API key required for basic usage

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from forex_api import get_eur_usd_price

# Fetch current EUR/USD rate
rate = get_eur_usd_price()
if rate is not None:
    print(f"EUR/USD: {rate:.4f}")
else:
    print("Failed to fetch exchange rate")
```

### With Fallback Support

```python
from forex_api import get_forex_price_with_fallback

# Fetch rate with automatic fallback to secondary API
rate = get_forex_price_with_fallback()
if rate is not None:
    print(f"EUR/USD: {rate:.4f}")
else:
    print("All APIs failed")
```

### Running the Module Directly

```bash
python forex_api.py
```

## Error Handling

The module handles the following error conditions gracefully:

- **Network timeouts**: 10-second timeout for API requests
- **Connection errors**: Network connectivity issues
- **HTTP errors**: API server errors (4xx, 5xx status codes)
- **Invalid JSON**: Malformed API responses
- **Missing data**: API responses without expected fields
- **Invalid rates**: Non-numeric or negative rate values

All errors are logged to the console and the function returns `None` instead of raising exceptions.

## Testing

Run the test suite:

```bash
python test_forex_api.py
```

The tests cover:
- Successful API calls
- Various error conditions
- Edge cases with invalid data
- Fallback functionality

## APIs Used

- **Primary**: exchangerate-api.com (free tier)
- **Fallback**: open.er-api.com (free tier)

Both APIs provide real-time exchange rates without requiring API keys for basic usage.

## Function Reference

### `get_eur_usd_price() -> Optional[float]`

Fetches the current EUR/USD exchange rate from the primary API.

**Returns:**
- `float`: The EUR/USD exchange rate
- `None`: If an error occurs

### `get_forex_price_with_fallback() -> Optional[float]`

Fetches the EUR/USD rate with automatic fallback to a secondary API if the primary fails.

**Returns:**
- `float`: The EUR/USD exchange rate
- `None`: If all APIs fail

## Requirements

- Python 3.6+
- requests library
- Internet connection for API access