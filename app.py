from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assets/<path:asset>")
def assets(asset):
    return send_from_directory("static/dist",asset)


if __name__ == "__main__":
    app.run(debug=True)
