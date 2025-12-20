from flask import Flask, render_template, Response, jsonify
from camera import *

app = Flask(__name__)

headings = ("Name", "Album", "Artist")
df1 = music_rec().head(15)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    global df1
    while True:
        frame, df1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/table_data')
def table_data():
    return jsonify(df1.to_dict(orient='records'))

@app.route('/detect_emotion')
def detect_emotion():
    emotion, confidence, song, artist, youtube = get_current_emotion()
    return jsonify({
        "emotion": emotion,
        "confidence": confidence,
        "song": song,
        "artist": artist,
        "youtube_link": youtube
    })

if __name__ == '__main__':
    app.run(debug=True)
