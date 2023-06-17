from flet import *;

def card_subview(page):

    #
    from ..components.title import title;
    from ..components.ccard import ccard;

    any_card = page.client_storage.contains_key("cards")
    content = None;

    if any_card :
        cards = page.client_storage.get("cards");
        content = Column()
        ccards_lists = [];

        for idx, data in enumerate(cards):
            if idx % 2 == 0:
                ccards_lists.append(ccard(page, data["alias"], data["card_number"], data["date"], data["cvv"], idx, True))
            else:
                ccards_lists.append(ccard(page, data["alias"], data["card_number"], data["date"], data["cvv"], idx))

        content.controls = ccards_lists;

    else:
        content = Text("Actually, you do not have any card registered...")

    return Container(
        content=Column(
            [
                title("My Credit Cards"),
                content
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.ALWAYS,
            height=370
        )
    )