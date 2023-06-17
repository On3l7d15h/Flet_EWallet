from flet import *;

def create_alert(page, form, tit, content):

    #
    from ..components.fill_btn import fill_btn;
    from ..components.title import title;

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
        actions=[fill_btn(page, "Cerrar", icons.CLOSE, close_alert, True),],
        actions_alignment=MainAxisAlignment.CENTER,
        modal=True,
        shape=RoundedRectangleBorder(radius=5),
        
    )
    alias = form.content.controls[1].controls[0].value;
    card_number = form.content.controls[2].controls[0].value;
    date = form.content.controls[3].controls[0].controls[0].value;
    cvv = form.content.controls[3].controls[1].controls[0].value;

    # validation
    if alias == None or alias == "":
        open_alert();
        return False;
    
    if card_number == None or card_number == "" or len(card_number) < 16:
        open_alert();
        return False;

    if date  == None or date == "" or len(date) < 5:
        open_alert();
        return False;
    
    if cvv == None or cvv == "" or len(cvv) < 3:
        open_alert();
        return False;

    if page.client_storage.contains_key("cards"):
        cards = page.client_storage.get("cards")
        new_card = {
            "alias": alias,
            "card_number": card_number,
            "date": date,
            "cvv": cvv
        }
        cards.append(new_card)
        page.client_storage.set("cards", cards)
    else:
        cards = []
        new_card = {
            "alias": alias,
            "card_number": card_number,
            "date": date,
            "cvv": cvv
        }
        cards.append(new_card)
        page.client_storage.set("cards", cards)

    print(page.client_storage.get("cards"))

    return True;