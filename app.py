"""
Lezioni-da-YouTube - YouTube Lesson Generator

This application extracts transcripts from YouTube videos and generates
structured lesson cards using AI processing.
"""

import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)


def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    
    Supports various YouTube URL formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    
    Args:
        url (str): YouTube URL
        
    Returns:
        str: Video ID or None if not found
    """
    # Pattern for various YouTube URL formats
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?(?:.*&)?v=([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_transcript(video_id):
    """
    Retrieve the transcript for a YouTube video.
    
    Prioritizes Italian ('it') language, falls back to English ('en'),
    and finally to any available language.
    
    Args:
        video_id (str): YouTube video ID
        
    Returns:
        str: Concatenated transcript text
        
    Raises:
        Exception: If transcript is not available or video is invalid
    """
    try:
        # Create an instance of the API
        api = YouTubeTranscriptApi()
        
        # Try to get transcript list
        transcript_list = api.list(video_id)
        
        # Try Italian first, then English as fallback
        try:
            transcript = transcript_list.find_transcript(['it', 'en'])
        except NoTranscriptFound:
            # If neither Italian nor English is available, try to get any available transcript
            try:
                # Get the first available transcript
                transcript = next(iter(transcript_list))
            except StopIteration:
                # No transcripts available at all
                raise NoTranscriptFound(video_id, [], transcript_list)
        
        # Fetch the transcript
        transcript_data = transcript.fetch()
        
        # Concatenate all text segments (transcript entries are dictionaries)
        full_text = " ".join([entry['text'] for entry in transcript_data])
        
        return full_text
        
    except TranscriptsDisabled:
        raise Exception("Le trascrizioni sono disabilitate per questo video.")
    except NoTranscriptFound:
        raise Exception("Nessuna trascrizione trovata per questo video.")
    except VideoUnavailable:
        raise Exception("Video non disponibile o ID non valido.")


def generate_lesson_from_text(transcript_text):
    """
    Generate a structured lesson card from the transcript text.
    
    This function processes the transcript and creates a markdown-formatted
    lesson card with the following structure:
    - Title
    - Summary
    - Key Concepts
    - Detailed Explanation
    - Important Formulas (if applicable)
    - Examples
    - Summary/Conclusions
    
    Args:
        transcript_text (str): Raw transcript text
        
    Returns:
        str: Markdown-formatted lesson card
    """
    # For MVP, we'll create a basic structure
    # In production, this would call an LLM API (OpenAI, Anthropic, etc.)
    
    # Helper function to escape markdown special characters
    def escape_markdown(text):
        """Escape markdown special characters to prevent formatting issues."""
        # Escape common markdown special characters
        special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '|']
        for char in special_chars:
            text = text.replace(char, '\\' + char)
        return text
    
    # Basic analysis of the transcript
    word_count = len(transcript_text.split())
    preview = transcript_text[:500] + "..." if len(transcript_text) > 500 else transcript_text
    
    # Escape markdown characters in preview and full transcript
    preview_escaped = escape_markdown(preview)
    transcript_escaped = escape_markdown(transcript_text)
    
    # Generate a structured lesson card
    lesson_card = f"""# 📚 Scheda di Lezione

## 📋 Informazioni Generali
- **Lunghezza trascrizione**: {word_count} parole
- **Lingua**: Italiano/Inglese

## 📝 Anteprima Trascrizione
{preview_escaped}

## 🎯 Obiettivi della Lezione
*Questa sezione conterrà gli obiettivi principali della lezione una volta integrata l'elaborazione AI.*

## 🔑 Concetti Chiave
*Questa sezione elencherà i concetti principali trattati nella lezione.*

1. Concetto 1
2. Concetto 2
3. Concetto 3

## 📖 Spiegazione Dettagliata
*Questa sezione conterrà una spiegazione approfondita degli argomenti trattati.*

### Argomento 1
Descrizione dettagliata...

### Argomento 2
Descrizione dettagliata...

## 🧮 Formule Importanti
*Se applicabile, questa sezione mostrerà le formule matematiche o fisiche trattate.*

## 💡 Esempi
*Questa sezione conterrà esempi pratici discussi nella lezione.*

## 📌 Riepilogo
*Questa sezione riassumerà i punti chiave della lezione.*

---

## 🔬 Nota per il Futuro
Per ottenere un'analisi completa e intelligente del contenuto, questa applicazione può essere integrata con:
- OpenAI GPT-4
- Anthropic Claude
- Google Gemini
- Altri modelli di linguaggio avanzati

Il modello AI analizzerà la trascrizione completa e genererà automaticamente:
- Titolo appropriato
- Riassunto
- Concetti chiave estratti
- Spiegazioni dettagliate
- Formule (se presenti)
- Esempi pratici
- Conclusioni

### 📄 Trascrizione Completa
<details>
<summary>Clicca per visualizzare la trascrizione completa</summary>

{transcript_escaped}

</details>
"""
    
    return lesson_card


def main():
    """Main Streamlit application."""
    
    # Page configuration
    st.set_page_config(
        page_title="Lezioni-da-YouTube",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Title and description
    st.title("📚 Lezioni-da-YouTube")
    st.markdown("""
    ### Genera schede di lezione strutturate da video YouTube
    
    Inserisci l'URL di un video di YouTube (preferibilmente una lezione di fisica) 
    e questa applicazione genererà automaticamente una scheda di lezione formattata 
    e facile da studiare.
    """)
    
    # Input section
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        youtube_url = st.text_input(
            "🔗 URL del Video YouTube",
            placeholder="https://www.youtube.com/watch?v=...",
            help="Incolla qui l'URL completo del video YouTube"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        generate_button = st.button("🚀 Genera Lezione", type="primary", use_container_width=True)
    
    # Processing section
    if generate_button:
        if not youtube_url:
            st.error("⚠️ Per favore, inserisci un URL di YouTube valido.")
            return
        
        # Extract video ID
        video_id = extract_video_id(youtube_url)
        
        if not video_id:
            st.error("❌ URL non valido. Assicurati di inserire un URL YouTube corretto.")
            st.info("""
            **Formati supportati:**
            - `https://www.youtube.com/watch?v=VIDEO_ID`
            - `https://youtu.be/VIDEO_ID`
            - `https://www.youtube.com/embed/VIDEO_ID`
            """)
            return
        
        # Show video preview
        st.success(f"✅ Video ID estratto: `{video_id}`")
        
        with st.expander("🎥 Anteprima Video", expanded=True):
            st.video(youtube_url)
        
        # Get transcript with loading spinner
        with st.spinner("🔄 Estrazione della trascrizione in corso..."):
            try:
                transcript_text = get_transcript(video_id)
                st.success(f"✅ Trascrizione estratta! ({len(transcript_text)} caratteri)")
            except Exception as e:
                st.error(f"❌ Errore: {str(e)}")
                st.info("""
                **Possibili cause:**
                - Il video non ha trascrizioni disponibili
                - Le trascrizioni sono state disabilitate dal creatore
                - Il video è privato o non disponibile
                - L'ID del video non è valido
                """)
                return
        
        # Generate lesson card with loading spinner
        with st.spinner("🤖 Generazione della scheda di lezione in corso..."):
            try:
                lesson_card = generate_lesson_from_text(transcript_text)
                st.success("✅ Scheda di lezione generata con successo!")
            except Exception as e:
                st.error(f"❌ Errore nella generazione della lezione: {str(e)}")
                return
        
        # Display the lesson card
        st.markdown("---")
        st.markdown("## 📖 Scheda di Lezione Generata")
        st.markdown(lesson_card)
        
        # Download button
        st.download_button(
            label="⬇️ Scarica Scheda di Lezione (Markdown)",
            data=lesson_card,
            file_name=f"lezione_{video_id}.md",
            mime="text/markdown"
        )
    
    # Footer
    st.markdown("---")
    # Use columns for centering without unsafe_allow_html
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown("**📚 Lezioni-da-YouTube - MVP v1.0**")
        st.caption("Creato con Streamlit 🎈 | Trascrizioni da YouTube Transcript API 📝")


if __name__ == "__main__":
    main()
