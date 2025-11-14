import reflex as rx
from app.states.document_upload_state import DocumentUploadState
from app.components.sidebar import page_layout


def document_upload_page() -> rx.Component:
    return page_layout(
        rx.el.div(
            rx.el.p(
                "Upload your documents here to be processed by the LoopScan AI. You can upload multiple files at once.",
                class_name="text-gray-400",
            ),
            rx.upload.root(
                rx.el.div(
                    rx.el.button("Select Files", class_name="text-white"),
                    class_name="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-600 rounded-lg cursor-pointer hover:bg-gray-800",
                ),
                id="upload1",
                on_drop=DocumentUploadState.handle_upload(
                    rx.upload_files(upload_id="upload1")
                ),
                accept={
                    "application/pdf": [".pdf"],
                    "text/plain": [".txt"],
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [
                        ".docx"
                    ],
                },
            ),
            rx.cond(
                DocumentUploadState.uploaded_files_info.length() > 0,
                rx.el.div(
                    rx.el.p(
                        f"{DocumentUploadState.uploaded_files_info.length()} file(s) uploaded successfully!",
                        class_name="text-green-400 font-semibold",
                    ),
                    rx.foreach(
                        DocumentUploadState.uploaded_files_info,
                        lambda file_info: rx.el.p(
                            file_info, class_name="text-gray-300"
                        ),
                    ),
                    rx.el.button(
                        rx.cond(
                            DocumentUploadState.is_processing,
                            rx.el.span(
                                rx.icon("loader", class_name="animate-spin mr-2"),
                                "Processing...",
                            ),
                            "Process Documents",
                        ),
                        on_click=DocumentUploadState.process_documents,
                        is_loading=DocumentUploadState.is_processing,
                        class_name="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50",
                    ),
                    rx.cond(
                        DocumentUploadState.is_processed,
                        rx.el.p(
                            "Documents processed and are now available for chat.",
                            class_name="text-green-400 mt-4",
                        ),
                        None,
                    ),
                    class_name="mt-4 p-4 bg-gray-800 rounded-lg",
                ),
                None,
            ),
            class_name="flex flex-col gap-4",
        )
    )