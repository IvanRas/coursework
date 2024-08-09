import os

import pandas as pd


PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_transactions_dictionary_excel(excel_path: str) -> list[dict]:
    """FAункция пути до EXCEL-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []
    try:
        excel_data = pd.read_excel(excel_path)
        len_, b = excel_data.shape
        for i in range(len_):
            if excel_data["Дата операции"][i]:
                transaction_list.append(
                    {
                        "date_of_operation": excel_data["Дата операции"][i],
                        "payment_date": excel_data["Дата платежа"][i],
                        "card_number": excel_data["Номер карты"][i],
                        "state": excel_data["Статус"][i],
                        "cashback": excel_data["Кэшбэк"][i],
                        "payment_amount": excel_data["Сумма платежа"][i],
                        "category": excel_data["Категория"][i],
                        "operationAmount": {
                            "operation_amount": str(excel_data["Сумма операции"][i]),
                            "currency": {
                                "name": excel_data["Валюта операции"][i],
                                "code": excel_data["Валюта платежа"][i],
                            },
                        },
                        "description": excel_data["Описание"][i],
                        "mcc": excel_data["MCC"][i],
                        "bonuses": excel_data["Бонусы (включая кэшбэк)"][i],
                        "investment_piggy_bank": excel_data["Округление на инвесткопилку"][i],
                        "amount_rounded": excel_data["Сумма операции с округлением"][i],
                    }
                )
            else:
                continue
    except Exception:
        return []
    return transaction_list
