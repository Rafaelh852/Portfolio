from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assets/<path:asset>")
def assets(asset):
    return send_from_directory("static/dist/",asset)

@app.route("/notebook/<notebook>")
def notebooks(notebook):
    return render_template("notebook.html",notebook=notebook)

@app.route("/collection/<notebook>")
def collection(notebook):
    # endpoint for the collection of notebooks
    return render_template(f"notebooks/{notebook}.html")


if __name__ == "__main__":
    app.run(debug=True)
