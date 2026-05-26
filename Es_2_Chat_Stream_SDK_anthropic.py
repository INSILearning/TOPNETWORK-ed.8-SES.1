import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversation_history = []

def chat_stream(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})

    full_response = ""
    print("Claude: ", end="", flush=True)

    # context manager per lo stream
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="Sei un assistente tecnico specializzato in Python.",
        messages=conversation_history,
    ) as stream:
        # Ogni token arriva appena generato — non aspetti la risposta completa
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text
        print()  # newline finale
    return full_response

if __name__ == "__main__":
    print("Inviando messaggio...")
    chat_stream("Ciao! Dimmi 3 caratteristiche principali del linguaggio Python in modo conciso.")
