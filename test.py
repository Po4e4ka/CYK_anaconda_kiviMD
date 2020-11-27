import sqlite3

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.toolbar import MDActionBottomAppBarButton

from Card import *

from kivy.core.window import Window

from functions import tab_build

import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)



# Залив текста киви в переменную-------------------------------------------------------
kivy_code = ''
with open("kivy_code.kv", 'r', encoding="utf-8") as f:
    for i in f.readlines():
        if i[0] != '#':
            kivy_code += i
# -------------------------------------------------------------------------------------

# Класс со списком задач --------------------------------------------------------------
class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
# -------------------------------------------------------------------------------------

class MainApp(MDApp):
    """
    Класс приложения
    colors - Список цветов, используемых в приложении
    card_list - Список заявок
    object_list - Список объектов
    buttons - Кнопки, действия с заявкой
    """
    colors = {"toolbar":[.257, .222, .218, 1],
              "card_bg":[.730,.695,.707,1],
              "text":[1,1,1,1]
    }

    card_list = Card_.bitrix_to_Card_list()
    object_list = {}
    buttons = {'check': 'Завершить',
               'bomb': 'Отмена',
               'arm-flex': 'Принято'}
    botom_buttons = []
    # ---------- Заполнение объект листа. Объект лист имеет в себе все таски, после идет удаление списка заявок
    for card in card_list:
        if not (card.adress in object_list):
            object_list[card.adress] = [card]
        else:
            object_list[card.adress].append(card)
    not_sort_objects = {"Несорт": object_list["Несорт"]}
    del object_list["Несорт"]
    del card_list
    # --------------------------

    def build(self):
        """
        В этом методе идет создание приложения. Старт
        :return:
        """
        Window.size = (600, 600)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(kivy_code)

    def on_start(self):
        """
        Выполняются дествия после старта приложения
        Создаю табы на основном экране
        :return:
        """
        tab_build(self, self.object_list, Tab)
        tab_build(self, self.not_sort_objects, Tab)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        """
        Метод прит переключениии таб(объектов)
        :param instance_tabs:
        :param instance_tab:
        :param instance_tab_label:
        :param tab_text:
        :return:
        """
        pass

    #-------------------------- Открытие заявки ---------------------------------------------------
    def card_open(self, widget):
        card = widget.card_inside
        self.root.transition = FadeTransition()
        self.root.current = 'card'
        self.root.ids.taskContext.ids.title_text.text = f"{card.adress}"
        self.root.ids.taskContext.ids.main_text.text = f"{card.text}"
        self.root.ids.taskContext.ids.datetime_text.text = f"{card.date[0][0]}\n{card.date[1][0]}"

        self.root.ids.title.title = f"Задача №{card.number}"
    # ------Возврат на начальный экран-------------------------------------------------------------------

    def callback(self):
        self.root.current = 'main'
    # -------------------------------------------------------------------------------------------------


    def button_click_open(self, button):
        print("open")
        for i in range(1,len(button.children)-1,2):
            if len(self.botom_buttons) <= 2:
                button.children[i + 1].bind(on_press=lambda x: self.dop_button_click(x))
            temp = button.children[i+1]
            temp.label = button.children[i]
            self.botom_buttons.append(temp)


    def button_click_close(self, button):
        print("close")

    def dop_button_click(self, botom_button):
        print("toc")
        print(botom_button.label.text)







MainApp().run()