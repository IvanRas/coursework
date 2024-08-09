from src.views import greeting


@greeting("2024-01-01 07:00:00")
def test_greeting_morning() -> None:
    assert greeting() == "Доброе утро"


@greeting("2024-01-01 13:00:00")
def test_get_greeting_day() -> None:
    assert greeting() == "Добрый день"


@greeting("2024-01-01 19:00:00")
def test_get_greeting_evening() -> None:
    assert greeting() == "Добрый вечер"


@greeting("2024-01-01 00:00:00")
def test_get_greeting_night() -> None:
    assert greeting() == "Доброй ночи"

    