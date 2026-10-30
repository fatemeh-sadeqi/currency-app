import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"


try:
    response = requests.get(url)
    data = response.json()
except requests.exceptions.RequestException:
    print("Connection error. Check your enternet.")
    exit()

if data["result"] != "success":
    print("API error. Check your API key.")
    exit()

try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Enter a number.")
    exit()

code = input("Enter code: ").upper()

try:
    rate = data["conversion_rates"][code]
    result = (amount * rate)
    print(f"{amount} USD = {result:.2f} {code}")
except KeyError:
    print("Currency code not found.")
