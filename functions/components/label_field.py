from flet import *;

def label_field(page, text, is_pass=False, want_counter=False, max=0, width=550, can_reveal=False):

    def on_type(e):
        e.control.counter_text = f"{len(e.control.value)}/{max}";
        page.update();

    if want_counter:
        return Column(
            [
                TextField(
                    password=is_pass,
                    text_size=15,
                    label=text,
                    border="underline",
                    border_color=colors.PRIMARY, 
                    counter_text=f"0/{max}",
                    max_length=max,
                    on_change=on_type,
                    width=width,
                    can_reveal_password=can_reveal
                )
            ]
        )
    else:
        return Column(
            [
                TextField(
                    password=is_pass,
                    text_size=15,
                    label=text,
                    border="underline",
                    border_color=colors.PRIMARY, 
                    width=width
                )
            ]
        )