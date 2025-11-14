import reflex as rx


def sidebar_link(text: str, href: str, icon: str) -> rx.Component:
    return rx.link(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.text(text),
        href=href,
        class_name=rx.cond(
            rx.State.router.page.path == href.lower(),
            "flex items-center gap-3 rounded-lg bg-gray-700 px-3 py-2 text-white transition-all hover:text-white",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-400 transition-all hover:text-white",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.image(src="/placeholder.svg", class_name="h-8 w-auto"),
                    rx.el.span("LoopScan AI", class_name="sr-only"),
                    href="/",
                    class_name="flex items-center gap-2 text-lg font-semibold text-white",
                ),
                class_name="flex h-14 items-center border-b border-gray-800 px-4 lg:h-[60px] lg:px-6",
            ),
            rx.el.div(
                rx.el.nav(
                    sidebar_link("Chat", "/", "message-circle"),
                    sidebar_link("Document Upload", "/document_upload", "file-up"),
                    sidebar_link("Advanced Search", "/advanced_search", "search"),
                    class_name="grid items-start gap-2 px-2 text-sm font-medium lg:px-4",
                ),
                class_name="flex-1",
            ),
            class_name="flex h-full max-h-screen flex-col gap-2",
        ),
        class_name="hidden border-r border-gray-800 bg-gray-950 md:block md:w-[220px] lg:w-[280px] flex-shrink-0",
    )


def page_layout(main_content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            rx.el.header(
                rx.el.h1(
                    rx.match(
                        rx.State.router.page.path,
                        ("/", "💬 LoopScan Chat"),
                        ("/document_upload", "📄 Document Upload"),
                        ("/advanced_search", "🔍 Advanced Search"),
                        "LoopScan AI",
                    ),
                    class_name="text-lg font-semibold md:text-2xl text-white",
                ),
                class_name="flex h-14 items-center gap-4 border-b border-gray-800 bg-gray-950/40 px-4 lg:h-[60px] lg:px-6",
            ),
            rx.el.main(
                main_content,
                class_name="flex flex-1 flex-col gap-4 p-4 lg:gap-6 lg:p-6",
            ),
            class_name="flex flex-col flex-1 min-h-screen bg-gray-900",
        ),
        class_name="flex w-full text-white",
    )