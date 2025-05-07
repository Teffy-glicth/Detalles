from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("menu.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")
@app.route("/memories")
def memories():
    return render_template("memories.html")

@app.route("/letter")
def letter():
    return render_template("letter.html")

@app.route("/Love")
def Love():
    return render_template("Love.html")

@app.route("/Ask")
def Ask():
    return render_template("Ask.html")

if __name__ == "__main__":
    app.run(debug=True)