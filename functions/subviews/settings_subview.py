from flet import *;

def settings_subview(page):

    #
    from ..components.title import title;
    from ..components.label_field import label_field;
    from ..components.fill_btn import fill_btn;
    from ..methods.color_method import inverse_color_method;
    from ..alerts.change_color_alert import change_color_alert;
    from ..settings.settings import Settings

    def on_click(any=None):
        ans = change_color_alert(page, container, "Oops!", "Please select a valid option.")

        if ans:
            Settings(page)

    #
    mydropdown = Dropdown(
        options=[
            dropdown.Option("AMBER"),
            dropdown.Option("BLUE"),
            dropdown.Option("RED"),
            dropdown.Option("GREEN"),
        ],
        border="underline",
        label="Select one of these:",   
    );

    mydropdown.value = inverse_color_method(page.client_storage.get("color"));

    container = Container(
        content=Column(
            [
               title("Settings"),
               mydropdown,
               fill_btn(page, "Change", icons.UPDATE, on_click, True),
               Text("Developed By On3l7d15h", size=12, color=colors.with_opacity(.5, colors.PRIMARY))
            ],
            expand=5,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )
    )

    return container;