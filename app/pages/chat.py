import reflex as rx
from app.states.chat_state import ChatState
from app.components.sidebar import page_layout


def message_bubble(message: dict) -> rx.Component:
    is_user = message["role"] == "user"
    return rx.el.div(
        rx.el.p(message["content"]),
        class_name=rx.cond(
            is_user,
            "bg-blue-600 text-white p-3 rounded-lg self-end",
            "bg-gray-700 text-white p-3 rounded-lg self-start",
        ),
        max_width="70%",
    )


def chat_page() -> rx.Component:
    return page_layout(
        rx.el.div(
            rx.el.div(
                rx.foreach(ChatState.messages, message_bubble),
                class_name="flex-1 overflow-y-auto p-4 flex flex-col gap-4",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.input(
                        placeholder="Ask me anything...",
                        name="prompt",
                        class_name="flex-1 bg-gray-800 border-none focus:ring-0 text-white rounded-lg p-2",
                    ),
                    rx.el.button(
                        rx.icon("send", class_name="h-5 w-5"),
                        type="submit",
                        class_name="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700",
                    ),
                    class_name="flex items-center gap-2 p-2 bg-gray-900/80 rounded-lg",
                ),
                on_submit=ChatState.handle_submit,
                reset_on_submit=True,
                width="100%",
            ),
            class_name="flex flex-col h-[calc(100vh-120px)]",
        )
    )