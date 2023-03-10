from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/artificial_life")
def artificial_life():
    return "this page artificial_life"


@app.route("/about")
def about():
    return "test_site"


if __name__=="__main__":
    app.run(debug=True)
