from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition, ScreenManager

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

from Card import *

from kivy.core.window import Window

from functions import tab_build

import ctypes
import time

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = {"toolbar": [.257, .222, .218, 1],
                       "card_bg": [.730, .695, .707, 1],
                       "text": [1, 1, 1, 1]
                       }
        self.menu = 0 # Переменная бокового меню в тулбаре
        self.botom_buttons = []
        self.buttons = {'check': 'Завершить',
                        'bomb': 'Отмена',
                        'arm-flex': 'Принято'}
        self.menu_items = [{"text":"Мои заявки"},
                           {"text":"Настройки"},
                           {"text":"Сменить пользователя"}
                           ]
        # ---------- Заполнение объект листа. Объект лист имеет в себе все таски
        self.object_list, self.not_sort_objects = None, None
        self.my_tasks = {}
        self.tab_list =[]
        self.my_nickname = "NopeFantasy"
        # --------------------------

        Window.size = (600, 600)

    @classmethod
    def object_list_creator(cls, card_list):
        """
        Функция создает словарь объектов, хранящий список тасков для этого объекта.
        Возвращает словари и последний словарь с одним ключом "несорт" и несортирвоанными задачами
        :param card_list:
        :return:
        """
        object_list = {}
        for card in card_list:
            if not (card.adress in object_list):
                object_list[card.adress] = [card]
            else:
                object_list[card.adress].append(card)
        return object_list, {"Несорт": object_list.pop("Несорт")}

    def build(self):
        """
        В этом методе идет создание приложения. Старт
        :return:
        """

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
        self.object_list, self.not_sort_objects = self.object_list_creator(Card_.bitrix_to_Card_list())
        self.tab_list = tab_build(self, self.object_list, Tab)
        self.tab_list = tab_build(self, self.not_sort_objects, Tab)
        self.menu = MDDropdownMenu(caller=self.root.ids.menu_button,
                                   items=self.menu_items,
                                   width_mult=4,
                                   callback=lambda instance: self.menu_press(instance))


    def refresh(self, **kwargs):
        self.stop()
        for tab in self.tab_list:
            self.root.ids.tabs.remove_widget(tab)
        self.run()

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

    def menu_press(self, instance):
        print(instance)

    # -------------------------- Открытие заявки ---------------------------------------------------
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