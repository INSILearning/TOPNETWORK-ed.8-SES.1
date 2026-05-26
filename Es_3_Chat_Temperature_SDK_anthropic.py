# Confronto temperature 0 (deterministico) vs 0.9 (variabile)
# sulla stessa identica domanda
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

DOMANDA = "Proponi un nome per una funzione Python che verifica se un utente è attivo"

def genera(temperature: float, n: int = 5) -> list:
    """Genera n risposte alla stessa domanda con la temperature data."""
    risposte = []
    for _ in range(n):
        resp = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=80,
            temperature=temperature,
            messages=[{"role": "user", "content": DOMANDA}],
        )
        risposte.append(resp.content[0].text.strip())
    return risposte

if __name__ == "__main__":
    print("=== TEMPERATURE 0  (deterministico) ===")
    for r in genera(temperature=0):   print(f"  {r}")

    print("\n=== TEMPERATURE 0.9 (variabile)  ===")
    for r in genera(temperature=0.9):  print(f"  {r}")
