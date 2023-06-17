from flet import *;

def change_color_alert(page, form, tit, content):

    #
    from ..components.fill_btn import fill_btn;
    from ..components.title import title;
    from ..methods.color_method import color_method;

    def close_alert():
        page.dialog = my_alert;
        my_alert.open = False;
        page.update();
    
    def open_alert():
        page.dialog = my_alert;
        my_alert.open = True;        
        page.update();

    # vars
    my_alert = AlertDialog(
        title=title(tit),
        content=Text(content, text_align=TextAlign.CENTER),
        actions=[fill_btn(page, "Close", icons.CLOSE, close_alert, True),],
        actions_alignment=MainAxisAlignment.CENTER,
        modal=True,
        shape=RoundedRectangleBorder(radius=5),
        
    )

    option = form.content.controls[1].value;

    # validation
    if option == None or option == "":
        open_alert();
        return False;
    

    new_color = color_method(option)
    page.client_storage.set("color", new_color)

    return True;