import asyncio
import os

from fastapi import Body, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from openai import AsyncOpenAI


SYSTEM_PROMPT = """\
You are a customer-support executive for our
Chatting Service app named Tomato.

Your job is to understand the customer's main
problem and provide a helpful, professional response
related to the chatting service.

Use professional, polite, and empathetic language.
If the user has an issue or is frustrated, acknowledge
their feelings using phrases such as:
"I understand your concern."
"I understand how frustrating this can be."
"I am really sorry for the trouble."
"Let me help you resolve this."

Give clear and concise solutions whenever possible.
Do not claim that you performed an action unless the
system actually allows you to perform that action.

If the user asks a question that is not related to
the chatting service, politely explain that you can
only assist with Tomato's chatting service and its
related features, policies, accounts, and technical issues.

Do not provide answers to unrelated questions.
"""

app = FastAPI(title="Tomato app API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncOpenAI()
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
history: list[dict[str, str]] = []
history_lock = asyncio.Lock()


@app.post("/api/chat", response_class=PlainTextResponse)
async def chat(message: str = Body(..., media_type="text/plain")) -> str:
    async with history_lock:
        history.append({"role": "user", "content": message})

        api_response = await client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=history,
            store=False,
        )
        answer = api_response.output_text

        history.append({"role": "assistant", "content": answer})
        return answer


@app.delete("/api")
async def clear_chat() -> Response:
    async with history_lock:
        history.clear()
    return Response(status_code=200)
