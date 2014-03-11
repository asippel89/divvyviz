import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def divvyviz():
    return flask.render_template("index.html")

@app.route("/wkday")
def render_large_weekday():
    return flask.render_template("large_wkday.html")


if __name__ == "__main__":

    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
