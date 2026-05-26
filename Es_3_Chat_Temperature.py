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

def genera(domanda: str, temperature: float, n: int = 5) -> list:
    """Genera n risposte alla stessa domanda con la temperature data."""
    risposte = []
    for _ in range(n):
        resp = client.chat.completions.create(
            model="anthropic/claude-opus-4.6-fast", # Utilizzo il modello Opus come da tua ultima preferenza
            max_tokens=80,
            temperature=temperature,
            messages=[{"role": "user", "content": domanda}],
        )
        risposte.append(resp.choices[0].message.content.strip())
    return risposte

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.withdraw()
    user_domanda = simpledialog.askstring(
        title="Test Temperature", 
        prompt="Inserisci la domanda da porre al modello per valutare la varianza:"
    )
    
    if user_domanda:
        print(f"Eseguendo test per la domanda: '{user_domanda}'\n")
        print("=== TEMPERATURE 0  (deterministico) ===")
        for r in genera(user_domanda, temperature=0):   
            print(f"  {r}")

        print("\n=== TEMPERATURE 0.9 (variabile)  ===")
        for r in genera(user_domanda, temperature=0.9):  
            print(f"  {r}")
    else:
        print("Nessuna domanda inserita. Uscita.")
