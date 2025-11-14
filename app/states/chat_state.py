import reflex as rx
import asyncio
from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


class ChatState(rx.State):
    messages: list[Message] = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]
    attached_files: list[str] = []

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        self.attached_files = []
        for file in files:
            upload_data = await file.read()
            output_path = rx.get_upload_dir() / file.filename
            with output_path.open("wb") as f:
                f.write(upload_data)
            self.attached_files.append(file.filename)

    @rx.event
    def clear_attached_files(self):
        self.attached_files = []

    @rx.event
    async def handle_submit(self, form_data: dict):
        prompt = form_data.get("prompt", "").strip()
        if not prompt and (not self.attached_files):
            return
        user_message = prompt
        if self.attached_files:
            file_list = ", ".join(self.attached_files)
            user_message += f"\n\n*Attached files: {file_list}*"
        self.messages.append({"role": "user", "content": user_message.strip()})
        attached_files_for_response = self.attached_files.copy()
        self.attached_files = []
        yield
        response = f"This is a placeholder response."
        if prompt:
            response = f"You asked: '{prompt}'. " + response
        if attached_files_for_response:
            response += f" I see you've attached {len(attached_files_for_response)} file(s): {', '.join(attached_files_for_response)}."
        self.messages.append({"role": "assistant", "content": ""})
        yield
        for word in response.split():
            self.messages[-1]["content"] += word + " "
            await asyncio.sleep(0.05)
            yield