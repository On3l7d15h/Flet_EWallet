from flet import *;

from .router import router;

def Settings(page):

    #
    color = None;

    if page.client_storage.contains_key("color"):
        color = page.client_storage.get("color")
    else: 
        page.client_storage.set("color", colors.AMBER)
        color = page.client_storage.get("color")

    page.window_width = 550;
    page.window_height = 520;
    page.route = "/"
    page.theme = Theme(
        color_scheme_seed=color
    )
    page.window_title_bar_buttons_hidden = True;
    page.window_title_bar_hidden = True;
    page.window_resizable = False;

    #
    router(page)

   
    