import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# --- Inizializzazione OpenRouter ---
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# La history è una lista gestita dal CLIENT
conversation_history = []

def chat_stream(user_message: str) -> str:
    # 1. Aggiungi il messaggio utente alla history
    conversation_history.append({"role": "user", "content": user_message})

    full_response = ""
    print("Modello: ", end="", flush=True)

    # 2. Invia TUTTA la history — con stream=True per ricevere la risposta progressivamente
    response = client.chat.completions.create(
        model="anthropic/claude-opus-4.6-fast", # Modello OpenRouter
        max_tokens=1024,
        messages=[
            {"role": "system", "content": "Sei un assistente tecnico specializzato in Python."},
            *conversation_history
        ],
        stream=True # Parametro fondamentale per lo streaming
    )
    
    # 3. Itera sui "pezzi" (chunk) della risposta man mano che arrivano
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end="", flush=True)
            full_response += content
            
    print()  # newline finale una volta finito lo stream
    return full_response

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.withdraw()
    user_msg = simpledialog.askstring(title="Chat Bot Stream", prompt="Inserisci il tuo messaggio per il modello:")
    
    if user_msg:
        print(f"Inviando messaggio: '{user_msg}'...\n")
        chat_stream(user_msg)
    else:
        print("Nessun messaggio inserito. Uscita.")
