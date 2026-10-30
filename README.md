# Currency app

A command-line app that converts US dollars to other currencies, written in Python.

## Features

- Convert USD to another currency using live exchange rates
- Handle invalid currency codes
- Handle invalid amounts
- Handle internet connection problems
- Handle invalid API keys

## Setup

1. Install Python 3.
2. Install the libraries:

```
pip install requests python-dotenv
```

3. Get a free API key from exchangerate-api.com.
4. Create a file named `.env` in the project folder and add this line (use your own key):

```
API_KEY=your-key-here
```

## How to run

```
python currency.py
```

## What I learned

- What an API is and how to call it with `requests`
- How to keep an API key safe with a `.env` file
- Handling errors like `KeyError` and connection problems