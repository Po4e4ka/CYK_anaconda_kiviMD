import datetime
import numpy.random as rd


class Card_:
    adress = 'null'
    text = 'null'
    data = datetime.datetime.now()
    status = 'null'
    def __init__(self, adr, text, date, st):
        self.adress = adr
        self.text = text
        self.data = date
        self.status = st

    def json_to_Card(self, json):
        self.adress, self.text = json['task']['title'].splt('.')[0], json['task']['title'].splt('.')[1]
        self.data = json['task']['createdDate']


    enum_adr = {0: "Test",
                1: 'Аврора 1',
                2: "Аврора 2",
                3: "София",
                4: "Мегалит",
                5: "Виктория",
                6: "Дачный",
                7: "Екатерина",
                8: "Форвард",
                9: "Авиатор"}

    @classmethod
    def TestCardCreator(cls, count):
        testCards = []
        for i in range(count):
            testCards.append(
                Card_(cls.enum_adr[rd.randint(0, len(cls.enum_adr))],
                                   'test',
                                   datetime.datetime.now(),
                                   'closed')
            )
        return testCards

