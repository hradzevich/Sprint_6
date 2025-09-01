from data import rental_options, scooter_color
from faker import Faker
import random as r
from datetime import datetime, timedelta
from data import faq_section_data

faker = Faker("ru_RU")

# Преобразует словарь FAQ в список кортежей для параметризации pytest
faq_section_data_pytest = []
for index, data in faq_section_data.items():
    faq_section_data_pytest.append((index, data["question"], data["answer"]))


# Генерирует необходимые для заказа данные пользователя за исключением станции метро
def generate_personal_data(metro_station):
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "address": faker.street_name() + " " + str(r.randint(1, 100)),
        "metro_station": metro_station,
        "phone_number": "+7" + str(r.randint(100000000, 999999999)),
    }


# Генерирует необходимые для заказа детали заказа
def generate_order_data():
    return {
        "start_date": datetime.now() + timedelta(days=r.randint(1, 7)),
        "rental_days": r.choice(rental_options),
        "color": r.choice(scooter_color),
        "comment": r.choice([faker.sentence(nb_words=6), None]),
    }
