import reflex as rx
from app.states.chat_state import ChatState, Message


def message_bubble(message: Message) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                rx.cond(message["role"] == "user", "user", "bot"), class_name="h-6 w-6"
            ),
            class_name="rounded-full bg-gray-700 p-2",
        ),
        rx.el.div(
            rx.el.p(message["content"]), class_name="rounded-lg bg-gray-700 p-3 text-sm"
        ),
        class_name=rx.cond(
            message["role"] == "user",
            "flex items-start gap-3 justify-end",
            "flex items-start gap-3",
        ),
    )


def chat_area() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.foreach(ChatState.messages, message_bubble),
            class_name="flex-1 overflow-auto p-4 space-y-4",
        ),
        class_name="flex flex-col h-full",
    )


def chat_input() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            rx.el.input(
                placeholder="Ask me anything...",
                name="prompt",
                class_name="flex-1 bg-transparent focus:outline-none",
                key=ChatState.prompt,
            ),
            rx.el.button(
                rx.icon("arrow-up", class_name="h-4 w-4"),
                type="submit",
                class_name="rounded-full bg-blue-500 p-2 text-white hover:bg-blue-600",
            ),
            on_submit=ChatState.handle_submit,
            class_name="flex items-center gap-2 rounded-lg border border-gray-600 bg-gray-800 p-2",
        ),
        class_name="border-t border-gray-600 bg-gray-900/50 p-4",
    )


def chat_interface() -> rx.Component:
    return rx.el.div(
        rx.el.header(
            rx.el.h1("LoopScan Chat", class_name="text-xl font-semibold"),
            class_name="flex h-[60px] items-center border-b border-gray-600 bg-gray-900/50 px-6",
        ),
        chat_area(),
        chat_input(),
        class_name="flex h-screen flex-1 flex-col bg-gray-900",
    )