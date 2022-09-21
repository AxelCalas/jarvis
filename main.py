from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola hermosa, 3513940806 ;) llamame</h1>"

app.run()
