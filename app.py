import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import MUSICA_SCHEMA, SYSTEM_INSTRUCTION

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app) # Isso permite que o HTML fale com o Python

def generate_musica(sentimento_texto):
    conteudo_prompt = f"Encontre uma música real para este sentimento: {sentimento_texto}"
    
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", 
        contents=conteudo_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=MUSICA_SCHEMA,
        )
    )
    return response.text

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    
    # Pegamos o texto que vem do Frontend
    sentimento = data.get("sentimento") 
    
    if not sentimento or len(sentimento) < 3:
        return jsonify({"status": "error", "message": "Texto muito curto!"}), 400
    
    try:
        resultado_json = generate_musica(sentimento)
        musica_dados = json.loads(resultado_json)
        
        return jsonify({
            "status": "success",
            "dados_musica": musica_dados
        }), 200
        
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)