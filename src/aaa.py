import datetime as dt
import os
import requests

from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")


def greeting():
    date_string = dt.datetime.now()
    hour = dt.datetime.now().hour
    print(date_string)
    if 6 <= hour < 12:
        print("Доброе утро")
        return "Доброе утро"
    elif 12 <= hour < 18:
        print("Добрый день")
        return "Добрый день"
    elif 18 <= hour < 24:
        print("Добрый вечер")
        return "Добрый вечер"
    else:
        print("Доброй ночи")
        return "Доброй ночи"


def realttimecurrencyexchangerate():
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=symbols&base=EUR"
    payload = {}
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers, data = payload)
    json_result = response.json()
    currency_amount = json_result["result"]

    status_code = response.status_code
    result = response.text
    return currency_amount


if __name__ == "__main__":
    realttimecurrencyexchangerate()
