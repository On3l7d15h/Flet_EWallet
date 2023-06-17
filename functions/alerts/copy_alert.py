from flet import *;

def copy_alert(page, tit, content):

    #
    from ..components.fill_btn import fill_btn;
    from ..components.title import title;
    from ..settings.router import router;

    def close_alert(any=None):
        page.dialog = my_alert;
        my_alert.open = False;
        page.update();
    
    def open_alert():
        page.dialog = my_alert;
        my_alert.open = True;        
        page.update();

    # vars
    my_alert = AlertDialog(
        title=title(tit, 40),
        content=Text(content, text_align=TextAlign.CENTER),
        actions=[
            fill_btn(page, "Close", icons.CLOSE, close_alert, True),
        ],
        actions_alignment=MainAxisAlignment.CENTER,
        modal=True,
        shape=RoundedRectangleBorder(radius=5),
    )

    open_alert();
