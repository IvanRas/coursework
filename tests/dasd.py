from unittest.mock import mock_open, patch

import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category(samp_transactions: pd.DataFrame, test_operations) -> None:
    df_transactions = pd.DataFrame(samp_transactions)
    print(df_transactions)
    current_datetime = "20.04.2023 12:00:00"
    category = "Еда"

    mock_open_func = mock_open()

    with patch("builtins.open", mock_open_func):
        result = spending_by_category(df_transactions, category, current_datetime).to_dict(orient="records")