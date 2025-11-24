from flask import Flask

app = Flask(__name__)

@app.route('/')
def root() -> str:
    return "<h1>Hello, World!</h1>"

app.run(debug=True, host="0.0.0.0")