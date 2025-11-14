import reflex as rx


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=url,
        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-400 transition-all hover:text-white",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("bot", class_name="h-6 w-6"),
                    rx.el.span("LoopScan AI", class_name="sr-only"),
                    href="#",
                    class_name="flex items-center gap-2 text-lg font-semibold md:text-base",
                ),
                class_name="flex h-[60px] items-center border-b px-6",
            ),
            rx.el.div(
                rx.el.nav(
                    sidebar_item("Chat", "message-circle", "/"),
                    sidebar_item("Document Upload", "upload", "#"),
                    sidebar_item("Advanced Search", "search", "#"),
                    class_name="grid items-start px-4 text-sm font-medium",
                ),
                class_name="flex-1 overflow-auto py-2",
            ),
            class_name="hidden border-r bg-gray-800/40 md:block",
        ),
        class_name="h-full w-64 flex-shrink-0",
    )