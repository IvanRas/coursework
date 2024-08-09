import datetime
import os

from src.utils import get_transactions_dictionary_excel
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def work_time():
    date_string = datetime.datetime.now()
    date_str = date_string.strftime('%H:%M')
    date = datetime.datetime.today()
    time_string = date.strftime('%H:%M')
    new_time_morn = time_string + datetime.timedelta(hours=6, minutes=00)
    new_time_day = time_string + datetime.timedelta(hours=12, minutes=00)
    new_time_evening = time_string + datetime.timedelta(hours=18, minutes=00)
    new_time_nights = time_string + datetime.timedelta(hours=24, minutes=00)

    print(date_string)
    if date_str < new_time_morn:
        print("Доброе ночи")
    elif new_time_morn < date_str < new_time_day:
        print("Добрый  утро")
    elif new_time_day < date_str < new_time_evening:
        print("Добрый  день")
    elif new_time_evening < date_str < new_time_nights:
        print("Добрый  вечер")
    else:
        print("error")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    return f"{card_number[:4]} {card_number[4:8]} **** "


def total_amount_of_expenses() -> dict:
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


def total_category(transactions: dict) -> dict:
    """Функция подсчета кешбэка."""
    cash = 0
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for i in transactions["cashback"]:
        cash += i
    return cash


def top_five(total: dict) -> dict:
    """Функция топа 5 расзодов"""
    top = []
    transactions =
    # нужно достать из total_amount_of_expenses() total и отсортировать по убыванию
    # после вывести первые 5
    for i in
        top.append(i)[:5]
    return top


def shares_sp500():
    """Функция подсчета Стоимость акций из S&P500."""
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%5EGSPC"
    headers = {"apikey": api_key}


if __name__ == "__main__":
    work_time()
