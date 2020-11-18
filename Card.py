import datetime
import numpy.random as rd


class Card_:
    def __init__(self, numb, adr, text, date, st):
        self.number = numb
        self.adress = adr
        self.text = text
        self.date = date
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
            obj = cls.enum_adr[rd.randint(0, len(cls.enum_adr))]
            testCards.append(
                Card_(i,
                      obj,
                      ''.join([chr(a) for a in range(65,90)]),
                      datetime.datetime.now(),
                      'closed')
            )
        return testCards

