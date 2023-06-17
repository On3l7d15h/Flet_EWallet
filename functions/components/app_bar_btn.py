from flet import *;

def app_bar_btn(page):

    return IconButton(
        icon=icons.CLOSE,
        on_click= lambda _: page.window_close(),
        style= ButtonStyle(
            shape=RoundedRectangleBorder(radius=5)
        )
    )