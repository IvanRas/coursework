import os

import pandas as pd
import requests
import datetime as dt

from src.utils import get_transactions_dictionary_excel
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.xlsx")

fileName = 'operations.xlsx'
df = excel_data = pd.read_excel("transactions_excel.xlsx")


def month_transaction():
    month_day = dt.datetime.now().day
    last_date = month_day


def greeting() -> str:
    hour = dt.datetime.now().hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_cart_transactions() -> list:
    """Функция вывода даных по одной карте."""
    cart_transactions = []
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["card_number"]:
        if i in cart_transactions:
            continue
        else:
            cart_transactions.append(i)
    return cart_transactions


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    return f"{card_number[-4:]}"


def total_amount_of_expenses(transaction_list: list[dict]) -> float:
    """Функция подсчета общих расходов."""
    # из столбца operation_amount/Сумма операции взять те что идут с минусом и составить
    # новый список включающий только расзоды
    total = 0
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["operation_amount"]:
        if i > 0:
            break
        else:
            total += i
    return total


def total_category(transaction_list: list[dict]) -> float:
    """Функция подсчета кешбэка."""
    cash = 0
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["cashback"]:
        cash += i
    return cash


def top_five(transaction_list: list[dict]) -> dict:
    top_transaction_list = []
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["operation_amount"]:
        if i < 0:
            top_transaction_list.append(i)
            top_transaction_list.sort()
        return top_transaction_list.index[:5]


def realttimecurrencyexchangerate() -> float:
    base = ["USD", "EUR"]
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=rubs&base={base}"
    payload = {}
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_result = response.json()
    currency_amount = json_result["result"]
    return currency_amount


if __name__ == "__main__":
    greeting()
    get_mask_card_number()
    total_amount_of_expenses()
    total_category()
    realttimecurrencyexchangerate()
