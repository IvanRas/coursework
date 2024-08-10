# -*- coding: utf-8 -*-

import json
import unittest

import pandas as pd

from src.services import transfers_to_individuals, transfers_to_phone


class TestTransfersToIndividuals(unittest.TestCase):

    def test_transfers_to_individuals(self) -> None:
        data = {
            "Категория": ["Переводы", "Переводы", "Расходы"],
            "Описание": ["Перевод Ивану И.", "Перевод Петрову П.", "Оплата услуг"],
        }
        transactions = pd.DataFrame(data)

        expected_output = json.dumps(
            [
                {"Категория": "Переводы", "Описание": "Перевод Ивану И."},
                {"Категория": "Переводы", "Описание": "Перевод Петрову П."},
            ],
            ensure_ascii=False,
            indent=4,
        )

        result = transfers_to_individuals(transactions)
        self.assertEqual(result, expected_output)


def test_transfers_to_phone() -> None:
    data = {
        "Описание": [
            "Перевод на номер +7 123 456-00-00",
            "Оплата услуги",
            "Перевод на номер +8 987 654-45-45",
            "Транзакция без номера",
            "Перевод на номер +7 777 777-88-00",
        ],
        "Сумма": [100, 200, 150, 300, 250],
    }

    df = pd.DataFrame(data)

    expected_result = [
        {"Описание": "Перевод на номер +7 123 456-00-00", "Сумма": 100},
        {"Описание": "Перевод на номер +8 987 654-45-45", "Сумма": 150},
        {"Описание": "Перевод на номер +7 777 777-88-00", "Сумма": 250},
    ]

    result = transfers_to_phone(df)
    result_json = json.loads(result)
    assert result_json == expected_result, f"Expected {expected_result}, but got {result_json}"
