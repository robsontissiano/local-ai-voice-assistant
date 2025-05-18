from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

@csrf_exempt
def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
        res = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
        answer = res.json().get("response", "No response.")
        return render(request, "dashboard/home.html", {"response": answer, "prompt": prompt})
    return render(request, "dashboard/home.html")
