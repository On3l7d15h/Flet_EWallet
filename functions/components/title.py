from flet import *;

def title(text, size=20):

    return Text(
        value=text,
        text_align=TextAlign.CENTER,
        width=550,
        size=size,
        weight=FontWeight.BOLD
    )