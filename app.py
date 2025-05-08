from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("menu.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/memories")  # Añadido espacio para mejor legibilidad
def memories():
    return render_template("memories.html")

@app.route("/letter")
def letter():
    return render_template("letter.html")

@app.route("/love")  # Cambiado a minúsculas para seguir convención
def love():         # Cambiado a minúsculas para seguir convención
    return render_template("Love.html")

@app.route("/ask")  # Cambiado a minúsculas para seguir convención
def ask():         # Cambiado a minúsculas para seguir convención
    return render_template("Ask.html")

@app.route("/no1")
def no1():
    return render_template("no1.html")

@app.route("/no2")
def no2():
    return render_template("no2.html")

@app.route("/si")
def si():
    return render_template("si.html")

if __name__ == "__main__":
    # En desarrollo
    app.run(debug=True)
else:
    # En producción
    app.run(host='0.0.0.0')