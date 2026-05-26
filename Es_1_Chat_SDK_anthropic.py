import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# La history è una lista gestita dal CLIENT — il server è stateless
conversation_history = []

def chat(user_message: str) -> str:
    # 1. Aggiungi il messaggio utente alla history
    conversation_history.append({"role": "user", "content": user_message})

    # 2. Invia TUTTA la history — il modello vede il contesto completo
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="Sei un assistente tecnico specializzato in Python.",
        messages=conversation_history,
    )
    return response.content[0].text

if __name__ == "__main__":
    print("Inviando messaggio...")
    risposta = chat("Ciao! Dimmi 3 caratteristiche principali del linguaggio Python in modo conciso.")
    print("\nRisposta del modello:")
    print(risposta)
