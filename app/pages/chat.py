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


def attached_files_display() -> rx.Component:
    return rx.cond(
        ChatState.attached_files.length() > 0,
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    ChatState.attached_files,
                    lambda f: rx.el.span(
                        rx.icon("file", class_name="h-4 w-4 mr-2"),
                        f,
                        class_name="flex items-center text-sm bg-gray-700 text-white px-2 py-1 rounded-md",
                    ),
                ),
                class_name="flex flex-wrap gap-2",
            ),
            rx.el.button(
                "Clear",
                on_click=[
                    ChatState.clear_attached_files,
                    rx.clear_selected_files("chat_upload"),
                ],
                class_name="text-xs text-gray-400 hover:text-white",
                size="1",
                variant="ghost",
            ),
            class_name="flex items-center justify-between p-2 bg-gray-900/50 rounded-t-lg border-b border-gray-700",
        ),
        None,
    )


def chat_page() -> rx.Component:
    return page_layout(
        rx.el.div(
            rx.el.div(
                rx.foreach(ChatState.messages, message_bubble),
                class_name="flex-1 overflow-y-auto p-4 flex flex-col gap-4",
            ),
            rx.el.div(
                attached_files_display(),
                rx.el.form(
                    rx.el.div(
                        rx.upload.root(
                            rx.el.button(
                                rx.icon("circle_plus", class_name="h-6 w-6"),
                                type="button",
                                class_name="text-gray-400 hover:text-white transition-colors",
                                variant="ghost",
                            ),
                            id="chat_upload",
                            multiple=True,
                            accept={
                                "application/pdf": [".pdf"],
                                "text/plain": [".txt"],
                                "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [
                                    ".docx"
                                ],
                            },
                            on_drop=ChatState.handle_upload(
                                rx.upload_files(upload_id="chat_upload")
                            ),
                            class_name="p-2 flex items-center justify-center",
                        ),
                        rx.el.input(
                            placeholder="Ask me anything...",
                            name="prompt",
                            class_name="flex-1 bg-transparent border-none focus:ring-0 text-white p-2",
                        ),
                        rx.el.button(
                            rx.icon("send", class_name="h-5 w-5"),
                            type="submit",
                            class_name="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700",
                        ),
                        class_name="flex items-center gap-2 p-1 bg-gray-800/80 rounded-b-lg",
                    ),
                    on_submit=ChatState.handle_submit,
                    reset_on_submit=True,
                    width="100%",
                ),
                class_name="border-t border-gray-800",
            ),
            class_name="flex flex-col h-[calc(100vh-120px)]",
        )
    )