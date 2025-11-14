import reflex as rx
from app.components.sidebar import sidebar
from app.components.chat import chat_interface
from app.states.chat_state import ChatState


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        chat_interface(),
        class_name="flex h-screen w-full bg-gray-900 text-white",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index, route="/")