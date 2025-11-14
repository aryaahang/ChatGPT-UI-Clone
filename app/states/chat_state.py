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

    @rx.event
    async def handle_submit(self, form_data: dict):
        prompt = form_data.get("prompt", "").strip()
        if not prompt:
            return
        self.messages.append({"role": "user", "content": prompt})
        yield
        response = f"You asked: '{prompt}'. This is a placeholder response."
        self.messages.append({"role": "assistant", "content": ""})
        yield
        for word in response.split():
            self.messages[-1]["content"] += word + " "
            await asyncio.sleep(0.05)
            yield