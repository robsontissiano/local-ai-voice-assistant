import sounddevice as sd
import vosk
import pyttsx3
import queue
import json
import requests

q = queue.Queue()
model = vosk.Model("vosk-model-small-en-us-0.15")
rec = vosk.KaldiRecognizer(model, 16000)
tts = pyttsx3.init()

OLLAMA_API = "http://localhost:11434/api/generate"

def speak(text):
    tts.say(text)
    tts.runAndWait()

def callback(indata, frames, time, status):
    if status:
        print(status)
    if rec.AcceptWaveform(bytes(indata)):
        result = json.loads(rec.Result())
        q.put(result.get("text", ""))

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎙️ Listening... (Ctrl+C to stop)")
        while True:
            text = q.get()
            if text:
                print(f"🗣️ You said: {text}")
                prompt = f"You are an assistant. Respond clearly. User: {text}"
                response = requests.post(OLLAMA_API, json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False
                }).json()
                answer = response.get("response", "No response.")
                print(f"🤖 Assistant: {answer}")
                speak(answer)

if __name__ == "__main__":
    listen()
