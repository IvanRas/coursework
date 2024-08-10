# -*- coding: utf-8 -*-

import datetime as dt
import json
import os
from datetime import datetime
from typing import Optional

import pandas as pd
import requests
from dotenv import load_dotenv

from src.logger import setting_logger

logger = setting_logger("utils")


def read_xlsx_file(file_path: str) -> pd.DataFrame | None:
    """Функция преобразования Excel-файла в DataFrame"""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        logger.warning("Файл не найден")
        return None
    except pd.errors.ParserError:
        logger.warning("Ошибка чтения файла")
        return None
    logger.info("Файл успешно открыт")
    return df


def greeting() -> str:
    """Функция, возращает приветствие в зависимости от текущего времени"""
    hour = dt.datetime.now().hour
    logger.info("Функция начала свою работу.")
    if 6 <= hour < 12:
        logger.info("Функция успешно завершила свою работу.")
        return "Доброе утро"
    elif 12 <= hour < 18:
        logger.info("Функция успешно завершила свою работу.")
        return "Добрый день"
    elif 18 <= hour < 24:
        logger.info("Функция успешно завершила свою работу.")
        return "Добрый вечер"
    else:
        logger.info("Функция успешно завершила свою работу.")
        return "Доброй ночи"


def get_top_five_transactions(transactions: pd.DataFrame) -> list[dict] | None:
    """Функция, принимает на вход DataFrame транзакций и
    возвращает список словарей с ТОП-5 транзакций по сумме платежа."""
    logger.info("Функция начала свою работу.")
    try:
        top_5_transactions = transactions.nlargest(5, "Сумма операции")
    except KeyError:
        logger.warning("Неверный ключ")
        return None
    except TypeError:
        logger.warning("Неверный тип данных")
        return None

    logger.info("Функция обрабатывает данные транзакций.")
    top_list = []
    for _, transaction in top_5_transactions.iterrows():
        transaction_dict = {
            "date": transaction.get("Дата операции")[:10],
            "amount": transaction.get("Сумма операции"),
            "category": transaction.get("Категория"),
            "description": transaction.get("Описание"),
        }
        top_list.append(transaction_dict)
    logger.info("Функция успешно завершила свою работу.")
    return top_list


def fetch_exchange_rates() -> list[dict[str, float]] | None:
    """Функция возвращает курс валют в рублях,указанных в файле user_setting.json"""
    logger.info("Функция начала свою работу.")
    os.chdir("..")
    try:
        with open(os.path.join(os.getcwd(), "user_setting.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.warning("Ошибка чтения json-файла")
        return None

    load_dotenv(".env")
    api_key = os.getenv("API_KEY_EXCHANGE_RATES")

    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB"
        response = requests.get(url)
        resp_data = response.json()
    except requests.exceptions.RequestException:
        logger.warning("Ошибка API запроса")
        return None

    data_list = [
        {key: round(1 / value, 2)}
        for key, value in resp_data.get("conversion_rates").items()
        if key in data.get("user_currencies")
    ]
    logger.info("Функция успешно завершила свою работу.")
    return data_list


def filter_transactions_by_date(
    transactions: pd.DataFrame, end_date: Optional[str | pd.DataFrame] = None
) -> pd.DataFrame:
    """Функция, фильтрации транзакций по дате.Формат даты: %d.%m.%Y %H:%M:%S"""
    logger.info("Функция начала свою работу.")
    if end_date is None:
        end_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    start_date = datetime.strptime(end_date, "%d.%m.%Y %H:%M:%S").replace(day=1)
    end_date = datetime.strptime(end_date, "%d.%m.%Y %H:%M:%S")
    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_transactions = transactions[
        (transactions["Дата операции"] >= start_date) & (transactions["Дата операции"] <= end_date)
    ]
    pd.options.mode.chained_assignment = None
    filtered_transactions["Дата операции"] = filtered_transactions["Дата операции"].dt.strftime("%d.%m.%Y %H:%M:%S")
    logger.info("Функция успешно завершила свою работу.")
    return filtered_transactions
