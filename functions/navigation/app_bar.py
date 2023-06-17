from flet import *;

def app_bar(page):

    # 
    from ..components.app_bar_btn import app_bar_btn;

    return AppBar(
        title=WindowDragArea(Text("Wallet")),
        actions=[
            app_bar_btn(page)
        ]
    )