from flet import *;

def update_alert(page, tit, content, idx):

    #
    from ..components.fill_btn import fill_btn;
    from ..components.label_field import label_field
    from ..components.title import title;
    from ..settings.router import router;

    def close_alert(any=None):
        page.dialog = my_alert;
        my_alert.open = False;
        page.update();
    
    def on_confirm(idx):

        # validation
        if alias.controls[0].value == None or alias.controls[0].value == "":
            return False;
        
        if card_number.controls[0].value == None or card_number.controls[0].value == "" or len(card_number.controls[0].value) < 16:
            return False;

        if date.controls[0].value  == None or date.controls[0].value == "" or len(date.controls[0].value) < 5:
            return False;
        
        if cvv.controls[0].value == None or cvv.controls[0].value == "" or len(cvv.controls[0].value) < 3:
            return False;

        cards = page.client_storage.get("cards")
        cards[idx] = {
            "alias": alias.controls[0].value,
            "card_number": card_number.controls[0].value,
            "date": date.controls[0].value,
            "cvv": cvv.controls[0].value
        }
        page.client_storage.set("cards", cards)

        page.dialog = my_alert;
        my_alert.open = False;
        page.update();
        router(page)
    
    def open_alert(idx):
        page.dialog = my_alert;
        my_alert.open = True;  

        cards = page.client_storage.get("cards")
        alias.controls[0].value = cards[idx]["alias"];
        card_number.controls[0].value = cards[idx]["card_number"];
        date.controls[0].value = cards[idx]["date"];
        cvv.controls[0].value = cards[idx]["cvv"];

        page.update();

    # vars
    alias = label_field(page, "Alias");
    card_number = label_field(page, "Card Number", False, True, 16);
    date = label_field(page, "Expire Date", False, True, 5, 200);
    cvv = label_field(page, "CVV", True, True, 3, 200, True);

    

    my_alert = AlertDialog(
        title=title(tit, 40),
        content=Column(
            [
                Text(content, text_align=TextAlign.CENTER),
                alias,
                card_number,
                Row(
                    [
                        date,
                        cvv
                    ],
                ),
            ],
            expand=5,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        ),
        actions=[fill_btn(page, "Close", icons.CLOSE, close_alert, True, None, False), fill_btn(page, "Update", icons.UPDATE, on_confirm, True, idx, True)],
        actions_alignment=MainAxisAlignment.CENTER,
        modal=True,
        shape=RoundedRectangleBorder(radius=5),
        
    )

    open_alert(idx)
