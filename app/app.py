import reflex as rx
from app.pages.chat import chat_page
from app.pages.document_upload import document_upload_page
from app.pages.advanced_search import advanced_search_page

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(chat_page, route="/")
app.add_page(document_upload_page, route="/document_upload")
app.add_page(advanced_search_page, route="/advanced_search")