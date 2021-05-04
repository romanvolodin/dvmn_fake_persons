from os import makedirs
from random import randint, sample

from faker import Faker

from file_operations import render_template


TOTAL_PERSONS = 10
MIN_POINTS = 8
MAX_POINTS = 14

SKILLS = [
    "Воет на луну",
    "Обожает очереди",
    "Спит в химзащите",
    "Рычит на айфоны",
    "Знает википедию наизусть",
    "Иммунитет к колбасе",
]

LETTERS = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


if __name__ == "__main__":
    runic_skills = [
        "".join([LETTERS[char] for char in skill]) for skill in SKILLS
    ]

    makedirs('result', exist_ok=True)

    for counter in range(1, TOTAL_PERSONS + 1):
        fake = Faker("ru_RU")

        skill_1, skill_2, skill_3 = sample(runic_skills, 3)

        person = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),

            "strength": randint(MIN_POINTS, MAX_POINTS),
            "agility": randint(MIN_POINTS, MAX_POINTS),
            "endurance": randint(MIN_POINTS, MAX_POINTS),
            "intelligence": randint(MIN_POINTS, MAX_POINTS),
            "luck": randint(MIN_POINTS, MAX_POINTS),

            "skill_1": skill_1,
            "skill_2": skill_2,
            "skill_3": skill_3,
        }

        render_template(
            "templates/charsheet.svg",
            f"result/person_{counter:04d}.svg", person
        )
