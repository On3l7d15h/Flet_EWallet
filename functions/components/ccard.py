from flet import *;
import pyperclip as pc;

def ccard(page, alias, number, date, ccv, idx, is_gray=False):

    # 
    from ..alerts.delete_alert import delete_alert
    from ..alerts.update_alert import update_alert
    from ..alerts.copy_alert import copy_alert
    from ..settings.router import router;

    saved_number = f"****  ****  ****  {number[12:16]}"

    def on_delete(idx):
        delete_alert(page, "Wait", "Are you sure you wanna delete this credit card?", idx)

    
    def on_update(idx):
        update_alert(page, "Credit Card", "Please fullfil the data you want to change:", idx)

    def on_copy_to_clipboard(idx):
        cards = page.client_storage.get("cards");
        pc.copy(f"{cards[idx]['card_number']}, {cards[idx]['date']}, {cards[idx]['cvv']}")
        copy_alert(page, "Successfully!", "Your card was copied to your clipboard!")


    if is_gray:
        return Card(
            elevation=20,
            color=colors.with_opacity(0.5, colors.BLACK45),
            content=Container(
                content=Column(
                    controls=[
                        Column(
                            [
                                Text(f"Bank Name", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY),
                                Row(
                                    [
                                        Text(alias, size=25, width=250),
                                        IconButton(
                                            icons.SETTINGS,
                                            on_click=lambda _: on_update(idx)
                                        ),
                                        IconButton(
                                            icons.COPY,
                                            on_click= lambda _: on_copy_to_clipboard(idx)
                                        ),
                                        IconButton(
                                            icons.DELETE,
                                            on_click= lambda _: on_delete(idx)
                                        )
                                    ],
                                 width=400,
                                )
                            ],
                            spacing=0,
                            horizontal_alignment=CrossAxisAlignment.START,
                            height=75
                        ),
                        Column(
                            [
                                Text(saved_number, size=40, text_align="center")
                            ],
                            horizontal_alignment= CrossAxisAlignment.CENTER,
                            width=400,
                            height=75
                        ),
                        Row(
                            [
                                Column(
                                    [
                                        Text("Date", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY),
                                        Text(date, size=17)
                                    ],
                                    width=133,
                                    height=55,
                                    spacing=0
                                ),
                                Column(
                                    [
                                        Text("CCV", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY), 
                                        Text(ccv, size=17),
                                    ],
                                    height=55,
                                    width=133,
                                    spacing=0
                                ),
                                Image(
                                    src="/images/mclogo.png", 
                                    height=65,
                                ),
                            ],
                            width=400,
                            vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,
                            alignment=CrossAxisAlignment.CENTER,

                        )
                    ],
                    spacing=0
                ),
                padding=5,
            )
        )
    else:
        return Card(
            elevation=20,
            content=Container(
                content=Column(
                    controls=[
                        Column(
                            [
                                Text(f"Bank Name", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY),
                                Row(
                                    [
                                        Text(alias, size=25, width=250),
                                        IconButton(
                                            icons.SETTINGS,
                                            on_click=lambda _: on_update(idx)
                                        ),
                                        IconButton(
                                            icons.COPY,
                                            on_click= lambda _: on_copy_to_clipboard(idx)
                                        ),
                                        IconButton(
                                            icons.DELETE,
                                            on_click= lambda _: on_delete(idx)
                                        )
                                    ],
                                 width=400,
                                )
                            ],
                            spacing=0,
                            horizontal_alignment=CrossAxisAlignment.START,
                            height=75
                        ),
                        Column(
                            [
                                Text(saved_number, size=40, text_align="center")
                            ],
                            horizontal_alignment= CrossAxisAlignment.CENTER,
                            width=400,
                            height=75
                        ),
                        Row(
                            [
                                Column(
                                    [
                                        Text("Date", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY),
                                        Text(date, size=17)
                                    ],
                                    width=133,
                                    height=55,
                                    spacing=0
                                ),
                                Column(
                                    [
                                        Text("CCV", weight=FontWeight.BOLD, size=15, color=colors.PRIMARY), 
                                        Text(ccv, size=17),
                                    ],
                                    height=55,
                                    width=133,
                                    spacing=0
                                ),
                                Image(
                                    src="/images/mclogo.png", 
                                    height=65,
                                ),
                            ],
                            width=400,
                            vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,
                            alignment=CrossAxisAlignment.CENTER,

                        )
                    ],
                    spacing=0
                ),
                padding=5,
            )
        )