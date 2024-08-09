import datetime
import os

from src.utils import get_transactions_dictionary_excel
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def work_time():
    date_string = datetime.datetime.now()
    time_obj = datetime.datetime(2022, 3, 8, 15, 45, 0)
    time_string = time_obj.strftime
    new_time_morn = time_string + datetime.timedelta(hours=6, minutes=00)
    new_time_day = time_string + datetime.timedelta(hours=12, minutes=00)
    new_time_evening = time_string + datetime.timedelta(hours=18, minutes=00)
    new_time_nights = time_string + datetime.timedelta(hours=24, minutes=00)

    print(date_string)
    if date_string < new_time_morn:
        print("Доброе ночи")
    elif new_time_morn < date_string < new_time_day:
        print("Добрый  утро")
    elif new_time_day < date_string < new_time_evening:
        print("Добрый  день")
    elif new_time_evening < date_string < new_time_nights:
        print("Добрый  вечер")
    else:
        print("error")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    return f"{card_number[:4]} {card_number[4:8]} **** "


def total_amount_of_expenses():
    """Функция подсчета общих расходов"""
    total = 0
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["operation_amount"]:
        if i > 0:
            break
        else:
            total += i
    return total


def total_category():
    """Функция подсчета общих расходов"""
    cash = 0
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["cashback"]:
        cash += i
    return cash


def top_five():
    """Функция подсчета общих расходов"""
    top = []
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["cashback"]:
        top.append(i)[:5]
    return top


def shares_sp500():
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%5EGSPC"
    headers = {"apikey": api_key}


if __name__ == "__main__":
    work_time()
