import reflex as rx
import asyncio
from typing import TypedDict, Literal


class Message(TypedDict):
    role: Literal["user", "assistant"]
    content: str


class ChatState(rx.State):
    messages: list[Message] = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]
    prompt: str = ""

    @rx.event
    async def handle_submit(self, form_data: dict):
        prompt = form_data["prompt"]
        if not prompt.strip():
            return
        self.messages.append({"role": "user", "content": prompt})
        yield
        self.prompt = ""
        yield
        yield ChatState.mock_response

    @rx.event
    async def mock_response(self):
        self.messages.append({"role": "assistant", "content": ""})
        assistant_response = f"You asked: '{self.messages[-2]['content']}'. This is a placeholder response."
        for chunk in assistant_response.split():
            self.messages[-1]["content"] += chunk + " "
            await asyncio.sleep(0.05)
            yield