from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
