import reflex as rx
import asyncio
from typing import TypedDict


class SearchResult(TypedDict):
    document_name: str
    snippet: str
    date: str


class AdvancedSearchState(rx.State):
    query: str = ""
    date_range_start: str = ""
    date_range_end: str = ""
    doc_types: list[str] = []
    doc_type_options: list[str] = ["pdf", "txt", "docx"]
    is_searching: bool = False
    results: list[SearchResult] = []
    show_warning: bool = False

    @rx.event
    def toggle_doc_type(self, doc_type: str):
        if doc_type in self.doc_types:
            self.doc_types.remove(doc_type)
        else:
            self.doc_types.append(doc_type)

    @rx.event
    def search(self):
        self.show_warning = False
        if not self.query.strip():
            self.show_warning = True
            return
        self.is_searching = True
        self.results = []
        yield
        yield asyncio.sleep(2)
        self.results = [
            {
                "document_name": "report_q1.pdf",
                "snippet": f"...found occurrence of **{self.query}** in the financial summary...",
                "date": "2023-03-31",
            },
            {
                "document_name": "meeting_notes.docx",
                "snippet": f"...action item related to **{self.query}** was assigned to John...",
                "date": "2023-04-12",
            },
            {
                "document_name": "data_analysis.txt",
                "snippet": f"...the analysis shows that **{self.query}** is a key factor...",
                "date": "2023-05-20",
            },
        ]
        self.is_searching = False