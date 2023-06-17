from flet import *;

def delete_alert(page, tit, content, index):

    #
    from ..components.fill_btn import fill_btn;
    from ..components.title import title;
    from ..settings.router import router;

    def close_alert(any=None):
        page.dialog = my_alert;
        my_alert.open = False;
        page.update();
    
    def confirm_alert(index):
        my_alert.open = False;
        cards = page.client_storage.get("cards")
        cards.pop(index);
        page.client_storage.set("cards", cards)
        page.update()
        router(page)
    
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
            fill_btn(page, "Delete", icons.DELETE, confirm_alert, True, index, True),
        ],
        actions_alignment=MainAxisAlignment.CENTER,
        modal=True,
        shape=RoundedRectangleBorder(radius=5),
    )

    open_alert();
   

    return True;