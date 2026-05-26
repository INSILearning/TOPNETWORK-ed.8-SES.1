import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# import anthropic
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# --- Inizializzazione Anthropic (Commentata) ---
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# --- Inizializzazione OpenRouter ---
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# La history è una lista gestita dal CLIENT — il server è stateless
conversation_history = []

def chat(user_message: str) -> str:
    # 1. Aggiungi il messaggio utente alla history
    conversation_history.append({"role": "user", "content": user_message})

    # 2. Invia TUTTA la history — il modello vede il contesto completo
    
    # --- Chiamata Anthropic (Commentata) ---
    # response = client.messages.create(
    #     model="claude-sonnet-4-5",
    #     max_tokens=1024,
    #     system="Sei un assistente tecnico specializzato in Python.",
    #     messages=conversation_history,
    # )
    # return response.content[0].text
    
    # --- Chiamata OpenRouter ---
    # Nota: su OpenRouter e nell'SDK OpenAI, il messaggio di "system" 
    # si passa all'inizio della lista dei messaggi invece che come parametro a sé
    response = client.chat.completions.create(
        model="anthropic/claude-opus-4.6-fast", # Nome corretto per OpenRouter
        max_tokens=1024,
        messages=[
            {"role": "system", "content": "Sei un assistente tecnico specializzato in Python."},
            *conversation_history
        ],
    )
    
    # Ritorna il testo della risposta
    return response.choices[0].message.content

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.withdraw()
    user_msg = simpledialog.askstring(title="Chat Bot", prompt="Inserisci il tuo messaggio per il modello:")
    
    if user_msg:
        print(f"Inviando messaggio: '{user_msg}'...")
        risposta = chat(user_msg)
        print("\nRisposta del modello:")
        print(risposta)
    else:
        print("Nessun messaggio inserito. Uscita.")
