import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template_string(open("index.html").read())


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
