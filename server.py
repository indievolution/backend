from flask import Flask, escape, request, send_file

app = Flask(__name__)

@app.route('/songs/')
def songlist():
    return "Hello"

@app.route('/song/<id>')
def get_song_info(id):
    try:
        return send_file("songs/Yumetourou (Kimi no Na wa.) [Huzure & Itsugo15].zip")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
