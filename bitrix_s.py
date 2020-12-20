from bitrix24 import Bitrix24, BitrixError
from json import dumps



class bitrix:
    bx24 = Bitrix24('https://icstech.bitrix24.ru/rest/86/c2v5jp0ukdwpv214')

    def get_group(self, responsible):  #
        try:
            rest = self.bx24.callMethod('tasks.task.list',
                                         filter={'GROUP_ID': '68',
                                                 "REAL_STATUS": "2",
                                                 "RESPONSIBLE_ID": responsible,
                                                 })  # 86 - Cipher
            # status 2 = pending task
            # status 5 = finished task
            # status 6 = delayed task
            return rest
        except BitrixError as message:
            return 0

    def switch_responsible(self, task, responsible):  #
        try:
            rest = self.bx24.callMethod('tasks.task.update',
                                        taskId=task,
                                        fields={"RESPONSIBLE_ID": f"{responsible}"}
                                        )
            return rest
        except BitrixError as massage:
            return 0


if __name__ == "__main__":
    byt = bitrix()
    print(dumps(byt.get_group()["tasks"], indent=4, ensure_ascii=False))
