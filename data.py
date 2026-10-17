from datetime import date, timedelta
from faker import Faker

fake = Faker("ru_RU")

def get_tomorrow():
    return (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")

ORDER_DATA = [
    {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": "Москва, улица Сретенский бульвар, дом 1",
        "metro": "Сретенский бульвар",
        "phone": fake.numerify("89#########"),
        "date": get_tomorrow(),
        "rental_period": "сутки",
        "color": "чёрный жемчуг",
        "comment": "Позвонить за час до доставки",
        "order_button": "top",
    },
    {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": "Москва, улица Сокольническая, дом 10",
        "metro": "Сокольники",
        "phone": fake.numerify("89#########"),
        "date": get_tomorrow(),
        "rental_period": "двое суток",
        "color": "серая безысходность",
        "comment": "Позвонить перед доставкой",
        "order_button": "buttom",
    },
]