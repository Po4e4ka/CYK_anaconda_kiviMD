import bitrix24
from bitrix24 import Bitrix24, BitrixError


class bitrix:
    bx24 = Bitrix24('https://icstech.bitrix24.ru/rest/86/c2v5jp0ukdwpv214')

    def get_group(self):  # get task by group id
        try:
            rest = self.bx24.callMethod('tasks.task.list',
                                         filter={'GROUP_ID': '68',
                                                 "REAL_STATUS":"2"})
            # status 2 = pending task
            # status 5 = finished task
            # status 6 = delayed task
            return rest
        except BitrixError as message:
            return 0

if __name__ == "__main__":
    byt = bitrix()
    print(byt.get_group())
