# 📚 Lezioni-da-YouTube

Un'applicazione web Python che genera schede di lezione strutturate da video YouTube.

## 🎯 Descrizione

**Lezioni-da-YouTube** è un'applicazione MVP (Minimum Viable Product) che permette di:
- Inserire un URL di un video YouTube (preferibilmente una lezione di fisica)
- Estrarre automaticamente la trascrizione del video
- Generare una scheda di lezione strutturata e formattata in Markdown
- Scaricare la scheda per studiare offline

## 🚀 Tecnologie Utilizzate

- **Python 3.8+**: Linguaggio di programmazione
- **Streamlit**: Framework web per l'interfaccia utente
- **youtube-transcript-api**: Libreria per estrarre trascrizioni da YouTube

## 📋 Prerequisiti

- Python 3.8 o superiore
- pip (gestore pacchetti Python)

## ⚙️ Installazione

1. Clona il repository:
```bash
git clone https://github.com/marcoodignoti/youtube-lesson-tool.git
cd youtube-lesson-tool
```

2. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

## 🎮 Utilizzo

1. Avvia l'applicazione:
```bash
streamlit run app.py
```

2. L'applicazione si aprirà automaticamente nel browser all'indirizzo `http://localhost:8501`

3. Inserisci l'URL di un video YouTube nel campo di testo

4. Clicca sul pulsante "🚀 Genera Lezione"

5. Attendi l'elaborazione (verrà mostrato uno spinner di caricamento)

6. Visualizza la scheda di lezione generata

7. Opzionalmente, scarica la scheda in formato Markdown

## 📝 Funzionalità

### ✅ Implementate (MVP)

- ✅ Input URL YouTube
- ✅ Estrazione automatica del Video ID
- ✅ Recupero trascrizione con priorità lingua italiana
- ✅ Fallback alla lingua inglese se italiano non disponibile
- ✅ Gestione errori elegante (trascrizioni disabilitate, video non disponibile)
- ✅ Anteprima video integrata
- ✅ Generazione scheda di lezione con struttura base
- ✅ Display formattato in Markdown
- ✅ Spinner di caricamento durante l'elaborazione
- ✅ Download della scheda in formato Markdown

### 🔮 Funzionalità Future (con integrazione AI)

L'applicazione è progettata per essere integrata con modelli di linguaggio avanzati come:
- OpenAI GPT-4
- Anthropic Claude
- Google Gemini
- Altri LLM

Con l'integrazione AI, la funzione `generate_lesson_from_text()` potrà:
- Analizzare il contenuto della trascrizione
- Identificare automaticamente i concetti chiave
- Generare riassunti intelligenti
- Estrarre formule matematiche/fisiche
- Creare esempi pratici
- Strutturare spiegazioni dettagliate

## 🏗️ Struttura del Progetto

```
youtube-lesson-tool/
├── app.py              # Applicazione principale Streamlit
├── requirements.txt    # Dipendenze Python
├── README.md          # Documentazione (questo file)
└── .gitignore         # File da ignorare in git
```

## 🔧 Architettura del Codice

### Funzioni Principali

#### `extract_video_id(url)`
Estrae il Video ID da un URL YouTube. Supporta vari formati:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

#### `get_transcript(video_id)`
Recupera la trascrizione di un video YouTube:
1. Tenta di ottenere la trascrizione in italiano ('it')
2. Se non disponibile, fallback all'inglese ('en')
3. Gestisce errori (trascrizioni disabilitate, video non disponibile)

#### `generate_lesson_from_text(transcript_text)`
Genera una scheda di lezione strutturata dal testo della trascrizione.
- **Versione MVP**: Crea una struttura base con la trascrizione
- **Versione futura**: Integrerà chiamate a LLM per analisi intelligente

#### `main()`
Funzione principale dell'applicazione Streamlit che gestisce:
- Configurazione della pagina
- Interfaccia utente
- Flusso di elaborazione
- Gestione errori
- Display dei risultati

## 🐛 Gestione Errori

L'applicazione gestisce elegantemente i seguenti casi:

| Errore | Gestione |
|--------|----------|
| URL non valido | Messaggio di errore con formati supportati |
| Trascrizioni disabilitate | Messaggio informativo |
| Video non disponibile | Notifica all'utente |
| Nessuna trascrizione trovata | Suggerimenti per risolvere |

## 🧪 Testing

Per testare l'applicazione, usa questi video di esempio:

1. Video con trascrizione italiana:
   ```
   https://www.youtube.com/watch?v=[VIDEO_CON_ITALIANO]
   ```

2. Video con trascrizione inglese:
   ```
   https://www.youtube.com/watch?v=[VIDEO_CON_INGLESE]
   ```

## 📚 Struttura della Scheda di Lezione

La scheda generata include le seguenti sezioni:

1. 📋 **Informazioni Generali**
2. 📝 **Anteprima Trascrizione**
3. 🎯 **Obiettivi della Lezione**
4. 🔑 **Concetti Chiave**
5. 📖 **Spiegazione Dettagliata**
6. 🧮 **Formule Importanti**
7. 💡 **Esempi**
8. 📌 **Riepilogo**
9. 📄 **Trascrizione Completa** (espandibile)

## 🔐 Privacy e Sicurezza

- ✅ Nessun dato viene salvato permanentemente
- ✅ Non vengono raccolte informazioni personali
- ✅ Le trascrizioni sono recuperate direttamente da YouTube
- ✅ Nessuna API key richiesta (per la versione MVP)

## 🤝 Contribuire

Contributi, problemi e richieste di funzionalità sono benvenuti!

## 📄 Licenza

Questo progetto è open source e disponibile per uso educativo.

## 👤 Autore

Marco Odignoti

## 🙏 Ringraziamenti

- Streamlit per il fantastico framework web
- youtube-transcript-api per l'accesso alle trascrizioni
- La comunità open source

---

**Nota**: Questa è una versione MVP. L'integrazione con modelli AI per l'elaborazione intelligente del testo sarà aggiunta in versioni future.
