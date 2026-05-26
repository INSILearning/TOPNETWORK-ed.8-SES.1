# Esercitazioni Python - API OpenRouter

Questo repository contiene tre esercizi pensati per esplorare l'interazione con i Large Language Models (LLM) tramite codice Python. 

## Perché OpenRouter invece di Anthropic?

I codici originali facevano affidamento sull'SDK nativo di Anthropic e sulla relativa chiave API. In questi esercizi, l'infrastruttura è stata adattata per utilizzare **OpenRouter** come intermediario, sfruttando la sintassi standard della libreria `openai`. 
Questa scelta è stata fatta per due motivi principali:
1. **Accessibilità e Costi**: OpenRouter permette di accedere a decine di modelli diversi (inclusa l'intera famiglia Claude di Anthropic) centralizzando il billing e spesso abbassando la barriera d'ingresso senza dover creare account multipli su vari provider.
2. **Standardizzazione**: Usando l'SDK di OpenAI, che è lo standard di fatto nell'industria, il codice diventa agnostico e portabile. Basterà cambiare la stringa del modello per passare istantaneamente da Claude a GPT-4, LLaMA o altri modelli, senza dover reimparare l'utilizzo di una nuova libreria.

---

## Gli Esercizi

### Es. 1 - Chat (`Es_1_Chat.py`)
Il primo esercizio introduce i concetti basilari di invio di un prompt al modello. È stato predisposto per inizializzare il client puntando a OpenRouter e lanciare un semplice messaggio tramite un pop-up interattivo all'avvio. Il modello utilizzato di default è `anthropic/claude-opus-4.6-fast`.

### Es. 2 - Chat Stream (`Es_2_Chat_Stream.py`)
Questo secondo script espande le funzionalità di base abilitando lo **streaming** della risposta. A differenza del primo esercizio, dove il programma attende che il modello abbia generato l'intera risposta prima di stamparla, qui l'opzione `stream=True` permette di mostrare a schermo i singoli token in tempo reale mano a mano che vengono prodotti. Questo riduce drasticamente la latenza percepita dall'utente.

### Es. 3 - Chat Temperature (`Es_3_Chat_Temperature.py`)
L'ultimo esercizio si concentra sul parametro `temperature`, che controlla il grado di creatività/varianza del modello.
Il programma chiede in input una domanda e la pone al modello in due cicli distinti:
- Un ciclo a `temperature=0`, in cui le risposte risultano puramente deterministiche, rigorose e quasi identiche tra loro.
- Un ciclo a `temperature=0.9`, che aumenta la creatività del modello generando risposte e strutture concettuali sempre diverse ad ogni interazione.
