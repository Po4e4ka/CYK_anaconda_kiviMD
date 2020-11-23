from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase, MDTabsBar
from kivymd.uix.list import ThreeLineAvatarIconListItem, MDList
from kivymd.uix.toolbar import MDActionBottomAppBarButton

from Card import *
from bitrix_s import bitrix

from kivy.core.window import Window

from functions import tab_build

Window.size = (400, 500)

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
    card_list = Card_.bitrix_to_Card_list()
    object_list = {}
    for card in card_list:
        if not (card.adress in object_list):
            object_list[card.adress] = [card]
        else:
            object_list[card.adress].append(card)
    not_sort_objects = {"Несорт":object_list["Несорт"]}

    del object_list["Несорт"]
    del card_list
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        return Builder.load_string(kivy_code)

    def on_start(self):
        tab_build(self,self.object_list, Tab)
        tab_build(self, self.not_sort_objects,Tab)


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

    def card_open(self, widget):
        card = widget.card_inside
        self.root.transition = FadeTransition()
        # self.root.transition.direction = 'down'
        self.root.current = 'card'
        self.root.ids.taskContext.ids.title_text.text = f"  {card.adress}"
        self.root.ids.taskContext.ids.main_text.text = f"{card.text}"
        self.root.ids.title.title = f"Задача №{card.number}"


    def callback(self):
        # self.root.transition.direction = 'up'
        self.root.current = 'main'

    def print_(self,toolbar):

        print(toolbar)

        button = MDActionBottomAppBarButton()
        button.data = {'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',}
        # button.rotation_root_button = True
        print(button.rotation_root_button)






MainApp().run()