from flask import Flask, request, jsonify, send_from_directory, send_file
import requests
import os
import tempfile
from dotenv import load_dotenv

app = Flask(__name__, static_folder='build', static_url_path='')

load_dotenv()

messages = []

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def post_message():
    new_message = request.json
    messages.append(new_message)
    return jsonify(new_message)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        temp_file_path = os.path.join(tempfile.gettempdir(), file.filename)
        file.save(temp_file_path)
        return jsonify({"message": "File uploaded successfully", "filename": file.filename})

@app.route('/api/tts', methods=['GET'])
def tts():
    text = request.args.get('text')
    response = requests.post(
        'https://api-inference.huggingface.co/models/facebook/wav2vec2-large-960h',
        headers={"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"},
        json={"inputs": text}
    )
    if response.status_code == 200:
        audio_data = response.content
        temp_audio_path = os.path.join(tempfile.gettempdir(), 'tts_output.wav')
        with open(temp_audio_path, 'wb') as audio_file:
            audio_file.write(audio_data)
        return send_file(temp_audio_path, mimetype='audio/wav')
    else:
        return 'Error with TTS', 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)