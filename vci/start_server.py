import requests
from SpeechSynthesizer import SpeechSynthesizer 
import flask
from flask import send_file
from flask import request
from flask import jsonify
from flask_cors import CORS
import sys

host = "0.0.0.0"


synthesizer= SpeechSynthesizer()

app = flask.Flask(__name__)
CORS(app)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.get_json()

    text = data.get('text')
    if not text:
        return jsonify({"error": "Text is required"}), 400

    if 'gpt_cond_len' in data:
        synthesizer.SetConditions(data['gpt_cond_len'])
    if 'temperature' in data:
        synthesizer.SetTemperature(data['temperature'])
    if 'stream' in data:
        synthesizer.SetStream(data['stream'])
    if 'audio_input' in data:
        synthesizer.SetInputWav(data['audio_input'])
    if 'output_wav' in data:
        synthesizer.SetOutputWaf(data['output_wav'])
    if 'language' in data:
        synthesizer.SetLanguge(data['language'])
    if 'sample_rate' in data:
        synthesizer.SetSampleRate(data['sample_rate'])
    if 'emotion' in data:
        synthesizer.SetEmotion(data['emotion'])

    audio_bytes = synthesizer.synthesize_speech(text)
    return send_file(audio_bytes, mimetype='audio/wav', as_attachment=True, download_name='synthesized_audio.wav')

if __name__ == '__main__':
    app.run(host=host, port=5200)