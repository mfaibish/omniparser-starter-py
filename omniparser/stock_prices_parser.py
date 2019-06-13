
import json
import os
import pandas

def calculate_latest_closing_price_from_json(filepath):
    with open(filepath,"r") as f:
        file_contents = f.read()
    
    stock_price = json.loads(file_contents)
    print(stock_price)

    return 10000

if __name__ == "__main__":
    print("PARSING SOME STOCK PRICES HERE...")

    stock_prices_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    
    latest_stock_price = calculate_latest_closing_price_from_json(stock_prices_filepath)

    print(latest_stock_price)