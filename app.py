from flask import Flask, send_from_directory

app = Flask(__name__)
app.debug=True



@app.route("/")   #127.0.0.1/
def index():
    return send_from_directory('html', "index.html")


@app.route('/<path:name>')   #127.0.0.1/
def start(name):
    return send_from_directory('html', name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    