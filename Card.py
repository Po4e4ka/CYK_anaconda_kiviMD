import datetime
import numpy.random as rd
from bitrix_s import bitrix
import re


class Card_:
    def __init__(self, numb, adr, text, date):
        self.number = numb
        self.adress = adr
        self.text = text
        self.date = date

    @classmethod
    def bitrix_to_Card_list(cls):
        bitrix_ = bitrix()
        task_list = bitrix_.get_group()["tasks"]
        card_list = []
        for i, task in enumerate(task_list):
            card_list.append(Card_(task['id'],
                                   cls.reg_test(task['title'], task),
                                   ' '.join([i.lstrip()+"/" for i in task['description'].split('/')[1:]]),
                                   re.findall(r"((\d\d\d\d-\d\d-\d\d)|(\d\d:\d\d:\d\d))",task['createdDate'])))
        return card_list

    @staticmethod
    def reg_test(title, task):
        enum_adr = [("Москва",["5-й предпортовый"]),
                    ("Философия",["1-й предпортовый"]),
                    ('Аврора 1',["Коллонтай", "Колонтай"]),
                    ("Аврора 2",["Белышева"]),
                    ("София",["ЮШ", "шоссе"]),
                    ("Мегалит",["Обуховской"]),
                    ("Виктория",["Авиаторов"]),
                    ("Дачный",["Дачный"]),
                    ("Екатерина",["Екатерининский д.2"]),
                    ("Форвард",["Цвета", "Екатерининская 22"]),
                    ("Авиатор",["Ручьевский"]),
                    ("Монплезир",["Ленинский"]),
                    ("СГ", ["Кравченко"])]
        for adr in enum_adr:
            if re.search(adr[0],title):
                return adr[0]
            else:
                for test in adr[1]:
                    if re.search(test, title) is not None:
                        return adr[0]
        print(task)
        return "Несорт"
