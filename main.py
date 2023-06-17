from flet import *;

from functions.settings.settings import Settings
from functions.views.main_view import main_view

def main(page: Page):
   
   Settings(page)

if __name__ == "__main__":
    app(target=main, assets_dir="assets")