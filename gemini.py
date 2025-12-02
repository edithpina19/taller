from flask import Flask, request, jsonify, render_template
from assistant import get_gemini_response  # Asegúrate de que tu función esté en assistant.py

app = Flask(__name__)


# RUTA PRINCIPAL (sirve el HTML de tu catálogo)
@app.route('/')
def index():
    # Asume que tienes un archivo HTML llamado 'index.html' en una carpeta 'templates'
    return render_template('index.html')


# RUTA DEL ASISTENTE (API)
@app.route('/api/gemini', methods=['POST'])
def gemini():
    # 1. Obtiene la pregunta enviada por el navegador
    data = request.get_json()
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"response": "Por favor, escribe una pregunta."}), 400

    # 2. Llama al modelo Gemini
    ai_response = get_gemini_response(user_prompt)

    # 3. Envía la respuesta de vuelta al navegador
    return jsonify({"response": ai_response})


if __name__ == '__main__':
    # Ejecuta el servidor en modo debug
    app.run(debug=True, port=5000)