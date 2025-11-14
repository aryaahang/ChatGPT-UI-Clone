import reflex as rx
import asyncio


class DocumentUploadState(rx.State):
    uploaded_files_info: list[str] = []
    is_processing: bool = False
    is_processed: bool = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        self.uploaded_files_info = []
        self.is_processed = False
        for file in files:
            upload_data = await file.read()
            self.uploaded_files_info.append(
                f"- {file.filename} ({len(upload_data) / 1024:.2f} KB)"
            )

    @rx.event
    def process_documents(self):
        self.is_processing = True
        yield
        yield asyncio.sleep(3)
        self.is_processing = False
        self.is_processed = True