
# Local AI Assistant

This is a fully local AI assistant that supports:

- Natural language interaction with Mistral 7B (via Ollama)
- File ingestion (PDFs)
- Web page ingestion (via URL)
- Voice interaction (speech-to-text and text-to-speech)

## How to Deploy

```bash
unzip local-ai-assistant-voice-final.zip
cd local-ai-assistant
docker compose up -d
docker exec -it ollama ollama pull mistral
```

Visit: http://localhost:5050



# Assistant Service (Django)

This is the main backend for the local AI assistant. It includes:

- REST endpoint to ask questions
- File upload for training from PDF
- URL ingestion
- Voice assistant loop using:
  - Vosk (speech-to-text)
  - pyttsx3 (text-to-speech)





## 🗣️ Voice Chat (Runs on Host)

1. Install required Python packages:
```bash
pip install vosk sounddevice pyttsx3 requests
```

2. Download and unzip the STT model:
```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
```

3. Run the voice assistant:
```bash
python voice_chat.py
```

Speak your prompt and the assistant will respond with audio.
