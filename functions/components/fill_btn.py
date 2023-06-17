from flet import *;

def fill_btn(page, text, icon, func={}, have_func=False, value=any, has_value=False):

    if have_func :
        return TextButton(
            text=text,
            icon=icon,
            style= ButtonStyle(
                shape=RoundedRectangleBorder(radius=5),
                bgcolor={
                    "": colors.PRIMARY_CONTAINER
                },
            ),
            on_click= lambda _: func(value if has_value == True else None)
        )
    else:
        return TextButton(
            text=text,
            icon=icon,
            style= ButtonStyle(
                shape=RoundedRectangleBorder(radius=5),
                bgcolor={
                    "": colors.PRIMARY_CONTAINER
                },
            ),
        )