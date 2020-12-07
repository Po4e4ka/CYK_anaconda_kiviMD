from kivymd.uix.list import ThreeLineAvatarIconListItem


def tab_build(app,object_list, Tab):
    tabs_list = []
    # Пройдусь по всем "названиям объекта"
    for name_tab in object_list.keys():
        # Сделаю список заявок в переменную с каждого объекта
        _card_list = object_list[name_tab]
        # Добавлю табу НОВОГО объекта
        tabs_list.append(Tab(text=name_tab))
        #
        app.root.ids.tabs.add_widget(tabs_list[-1])
        # Заполню заявками табу
        for card in _card_list:
            new_widget = ThreeLineAvatarIconListItem(text=f'Задача № {card.number}',
                                                     secondary_text=f"{card.date[0][0]}\n{card.date[1][0]}",
                                                     tertiary_text=card.text,

                                                     bg_color=[.183,.339,.262,.5],

                                                     theme_text_color="Custom",
                                                     secondary_theme_text_color= "Custom",
                                                     tertiary_theme_text_color="Custom",

                                                     text_color=[1,1,1,1],
                                                     secondary_text_color=[1,1,1,1],
                                                     tertiary_text_color=[1,1,1,1])
            new_widget.card_inside = card
            new_widget.bind(on_press=lambda t: app.card_open(t))

            tabs_list[-1].ids.main_list.add_widget(new_widget)

    return tabs_list
