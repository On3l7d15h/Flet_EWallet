from flet import *;

from ..views.main_view import main_view

def router(page):
     # Running app
    page.views.clear()
    page.views.append(main_view(page))
    page.update()