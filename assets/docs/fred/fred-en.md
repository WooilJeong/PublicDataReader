# FRED (Federal Reserve Economic Data) Usage Guide

[FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/) is an economic dataset provided by the Federal Reserve Bank of St. Louis. To use the FRED API, you will need an authentication key. You can obtain the authentication key by completing a simple form at [FRED API Key](https://fredaccount.stlouisfed.org/apikey). For a detailed guide on how to apply for the FRED API and to see real-life examples of key economic indicator inquiries, please refer to the blog post [Python for FRED: Exploring Economic Data](https://wooiljeong.github.io/python/pdr-fred/).

## How to Install PublicDataReader

1. Choose one of the following depending on your Operating System (OS):

- Windows: Run CMD (Command Prompt)
- Mac: Run Terminal

2. Enter and execute the following Shell command:

```bash
pip install PublicDataReader --upgrade
```

## Importing the Library

```python
from PublicDataReader import Fred

# FRED API key
api_key = "YOUR FRED API KEY"

# Create an instance
api = Fred(api_key)
```

## Searching for a Series

A 'series' in FRED represents the changes in a specific economic indicator over time. These series express changes in economic indicators over time through a series of continuous data points. Each series represents a specific economic indicator (e.g., unemployment rate, GDP, inflation, etc.) and this data is collected over a specific period (days, months, quarters, years, etc.). These series are helpful in analyzing and understanding economic patterns and trends. To search for such series, input `series_search` for `api_name` and the keyword of the series you wish to search for `search_text` in the `api.get_data()` method. From the search results, you can find the ID value of the series you want. This series ID value is used when querying series data. For instance, to find the series ID value of the consumer price index, an indicator related to inflation, input `consumer price index` for `search_text`.

```python
search_text = "consumer price index"
result = api.get_data(api_name="series_search", search_text=search_text)
result.head()
```

## Querying Series Data

To query series data, input `series_observations` for `api_name` and the series ID value for `series_id` in the `api.get_data()` method. For instance, to query the data series of the consumer price index, input `CPIAUCNS` for `series_id`. Note that this data can also be checked on the [FRED website](https://fred.stlouisfed.org/series/CPIAUCNS).

```python
# Series ID value
series_id = "CPIAUCNS"

# Query series data
df = api.get_data(api_name="series_observations", series_id=series_id)
df.tail()
```