from flet import *;

def main_view(page):

    #
    from ..navigation.app_bar import app_bar;
    from ..subviews.card_subview import card_subview
    from ..subviews.create_subview import create_subview
    from ..subviews.settings_subview import settings_subview
    
    #
    home = card_subview(page)
    card = create_subview(page)
    settings = settings_subview(page)

    home.visible = True;
    card.visible = False;
    settings.visible = False;

    def change_tab(e):
        index = e.control.selected_index

        home.visible = True if index == 0 else False;
        card.visible = True if index == 1 else False; 
        settings.visible = True if index == 2 else False; 

        page.update();       

    return View(
        route = "/",
        controls=[
            home,
            card,
            settings
        ],
        appbar=app_bar(page),
        navigation_bar=NavigationBar(
            selected_index=0,
            destinations=[
                NavigationDestination(label="Home", icon=icons.HOME),
                NavigationDestination(label="Card", icon=icons.CARD_TRAVEL),
                NavigationDestination(label="Settings", icon=icons.SETTINGS),
            ],
            on_change=change_tab,
            height=70
        )
    )