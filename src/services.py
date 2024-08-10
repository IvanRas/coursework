import os
import re

import pandas as pd

from src.utils import get_transactions_dictionary_excel


PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.xlsx")

fileName = 'operations.xlsx'
df = pd.read_excel("transactions_excel.xlsx")


def filter_by_name() -> dict:
    """функция по переводовe физическим лицам"""
    name = input("Введите имя: ")
    found_operations = []
    transactions = get_transactions_dictionary_excel(PATH_TO_FILE_EXCEL)
    for operation in transactions:
        if re.search(name, operation.get("description", "")):
            found_operations.append(operation)
        return found_operations
