from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import SlideTransition, CardTransition, RiseInTransition, FallOutTransition, FadeTransition

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase, MDTabsBar
from kivymd.uix.list import ThreeLineAvatarIconListItem, MDList
from kivymd.uix.toolbar import MDActionBottomAppBarButton

from Card import *
from bitrix_s import bitrix

from kivy.core.window import Window
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
    card_list = Card_.TestCardCreator(10)
    object_list = {}
    for card in card_list:
        if not (card.adress in object_list):
            object_list[card.adress] = [card]
        else:
            object_list[card.adress].append(card)
        print(card.number)
    del card_list
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        return Builder.load_string(kivy_code)

    def on_start(self):
        # Создам список таб, то есть объектов (Авр1, Авр2 и тд...)
        tabs_list = []
        # Пройдусь по всем "названиям объекта"
        for name_tab in self.object_list.keys():
            # Сделаю список заявок в переменную с каждого объекта
            _card_list = self.object_list[name_tab]
            # Добавлю табу НОВОГО объекта
            tabs_list.append(Tab(text=name_tab))
            #
            self.root.ids.tabs.add_widget(tabs_list[-1])
            # Заполню заявками табу

            for card in _card_list:
                print(card)
                new_widget = ThreeLineAvatarIconListItem(text=f'Задача № {card.number}',
                                                         secondary_text=str(card.date),
                                                         tertiary_text=card.status)
                new_widget.card_inside = card
                new_widget.bind(on_press=lambda t: self.card_open(t))

                tabs_list[-1].ids.main_list.add_widget(new_widget)


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
        print(self.root.ids.taskContext.ids)
        self.root.ids.taskContext.ids.title_text.text = f"  {card.adress}"
        self.root.ids.taskContext.ids.main_text.text = f"   {card.text}"*3
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