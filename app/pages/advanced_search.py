import reflex as rx
from app.states.advanced_search_state import AdvancedSearchState
from app.components.sidebar import page_layout


def result_card(result: dict) -> rx.Component:
    return rx.el.div(
        rx.el.h3(result["document_name"], class_name="font-semibold text-white"),
        rx.el.p(result["snippet"], class_name="text-sm text-gray-400"),
        rx.el.p(f"Date: {result['date']}", class_name="text-xs text-gray-500"),
        class_name="p-4 bg-gray-800 rounded-lg border border-gray-700",
    )


def advanced_search_page() -> rx.Component:
    return page_layout(
        rx.el.div(
            rx.el.p(
                "Use the filters below to perform an advanced search across your uploaded documents.",
                class_name="text-gray-400",
            ),
            rx.el.div(
                rx.el.input(
                    placeholder="Enter keywords, phrases, or questions...",
                    on_change=AdvancedSearchState.set_query,
                    class_name="w-full bg-gray-800 border-gray-700 text-white rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Date Range", class_name="text-sm font-medium text-white"
                        ),
                        rx.el.div(
                            rx.el.input(
                                type="date",
                                on_change=AdvancedSearchState.set_date_range_start,
                                class_name="bg-gray-800 border-gray-700 text-white rounded-lg p-2",
                            ),
                            rx.el.input(
                                type="date",
                                on_change=AdvancedSearchState.set_date_range_end,
                                class_name="bg-gray-800 border-gray-700 text-white rounded-lg p-2",
                            ),
                            class_name="flex gap-2",
                        ),
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Document Type", class_name="text-sm font-medium text-white"
                        ),
                        rx.el.div(
                            rx.foreach(
                                AdvancedSearchState.doc_type_options,
                                lambda doc_type: rx.el.label(
                                    rx.checkbox(
                                        doc_type,
                                        on_change=lambda checked: AdvancedSearchState.toggle_doc_type(
                                            doc_type
                                        ),
                                        checked=AdvancedSearchState.doc_types.contains(
                                            doc_type
                                        ),
                                    ),
                                    rx.el.span(doc_type.upper()),
                                    class_name="flex items-center gap-2 text-sm text-white",
                                ),
                            ),
                            class_name="flex gap-4 items-center",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4",
                ),
                rx.el.button(
                    rx.cond(
                        AdvancedSearchState.is_searching,
                        rx.el.span(
                            rx.icon("loader", class_name="animate-spin mr-2"),
                            "Searching...",
                        ),
                        "Search",
                    ),
                    on_click=AdvancedSearchState.search,
                    is_loading=AdvancedSearchState.is_searching,
                    class_name="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50",
                ),
                rx.cond(
                    AdvancedSearchState.show_warning,
                    rx.el.p(
                        "Please enter a search query.",
                        class_name="text-yellow-400 mt-2",
                    ),
                    None,
                ),
                class_name="p-4 border border-gray-700 rounded-lg bg-gray-800/50",
            ),
            rx.cond(
                AdvancedSearchState.results.length() > 0,
                rx.el.div(
                    rx.el.h2(
                        "Search Results", class_name="text-xl font-semibold mt-6 mb-4"
                    ),
                    rx.el.div(
                        rx.foreach(AdvancedSearchState.results, result_card),
                        class_name="flex flex-col gap-4",
                    ),
                ),
                None,
            ),
            class_name="flex flex-col gap-4",
        )
    )