from flet import *;

def create_subview(page):

    #
    from ..components.title import title;
    from ..components.label_field import label_field;
    from ..components.fill_btn import fill_btn;
    from ..alerts.create_alert import create_alert;
    from ..settings.router import router

    def on_create(any=None):
        ans = create_alert(page, container, "Oops!", "There are some fields empty or not correctly... please fill out those fields.")
        if ans:
            router(page);

    container = Container(
        content=Column(
            [
               title("Add Credit Card"),
               label_field(page, "Alias"),
               label_field(page, "Card Number", False, True, 16),
               Row(
                    [
                        label_field(page, "Expire Date", False, True, 5, 260),
                        label_field(page, "CVV", True, True, 3, 250, True)
                    ],
               ),
                fill_btn(page, "Create", icons.CREATE, on_create, True, has_value=False)
            ],
            expand=5,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )
    )

    return container;