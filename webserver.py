import flask
from flask import send_file,Flask,Response

app = Flask(__name__)



@app.route('/')
def home():
    return "Welcome to the server"

@app.route('/send_audio')
def audio_method():
    path_to_file = "/output.mp3"
    return send_file("C:/Users/91720/PycharmProjects/voiceRek/output.mp3",mimetype="audio/mp3",as_attachment=True,attachment_filename="output.mp3")

@app.route('/audio_stream')
def stream():
    def generate():
        with open("vathi.mp3","rb") as fwas:
            data = fwas.read(1024)
            while data:
                yield data
                data = fwas.read(1024)
    return Response(generate(),mimetype="audio/mp3")
if __name__ == "__main__":
    app.run()