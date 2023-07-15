from flask import Flask

app = Flask(__name__, instance_relative_config=True)


@app.route("/")
def index():
    return "<html><h1>Hello world</h1></html>"


@app.route("/healthcheck")
def healthcheck():
    return "OK"
