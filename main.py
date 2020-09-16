from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty


from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string('''
<all_this_shit>
    BoxLayout:
    
        NavigationLayout:
        
            ScreenManager:
                id: screen_manager
                Screen:
                    name: "arbeit_menu"
                    MDTabs:
                        id: tabs
                    MDBottomAppBar:
                        orientation: 'vertical'
    
                        MDToolbar:
                            id: toolbar
                            title: "ЦУК"
                            type: "bottom"
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            on_action_button: root.mid_button()
                            mode: "end"                  

                        Widget:
                        
                Screen:
                    name: "or_CYKA"
                                        
                    MDLabel:
                        text: "АААААА, бляяяяять\\nХули ничего не работаеееет!!?!?!??"
                        halign: "center" 
                    MDFloatingActionButton:
                        icon: "keyboard-backspace"
                        md_bg_color: app.theme_cls.primary_color   
    
            MDNavigationDrawer:
                id: nav_drawer
    
                ContentNavigationDrawer:                
                    id: con_nav_drawer
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
                    
            
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
        
        
<ContentNavigationDrawer>:
    id: con
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "kivymd.png"

    MDLabel:
        text: "Меню рабочее"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "ОПГ 'Центр удовлетворения клиентов'"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:
        id: scr
        DrawerList:
            id: md_list
            
            ItemDrawer:
                icon: "air-horn"
                text: "Крики цука"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "or_CYKA"
            
            ItemDrawer:
                icon: "fire"
                text: "Горящие жопы"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "arbeit_menu"
                
            ItemDrawer:
                icon: "format-text"
                text: "Пожаловаться тов.Майору"
            
            
            
            
<Tab>:
    
'''
)


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ContentNavigationDrawer(BoxLayout):
    """"""
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()





class all_this_shit(MDBoxLayout):
    """Здесь основной класс.
        Для доступа к его методам внутри него используется root.method_name
        События находятся в документации kivy"""
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print("left")

    def mid_button(self):
        print("mid_button_action")


class Tab(FloatLayout, MDTabsBase):
    '''Все, что происходит в основной части экрана'''
    def pop(self):
        self.ids.but.text = 'Lol'

class MainApp(MDApp):
    """
    Основной класс - точка входа.
    Для доступа к методам используется app.method_name
    """
    def build(self):
        return all_this_shit()

    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(text=f"Аврора 1"))
        self.root.ids.tabs.add_widget(Tab(text=f"Аврора 2"))
        self.root.ids.tabs.add_widget(Tab(text=f"София"))
        self.root.ids.tabs.add_widget(Tab(text=f"Екатерина"))
        self.root.ids.tabs.add_widget(Tab(text=f"Виктория"))

        # Разобрался, как получить доступ к элементу класса
        # Для доступа к сторонним классам в основном создается объект этого касса, ему дается индетификатор
        # и после этого, через его id можно получить доступ к его ids
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.con_nav_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )




MainApp().run()