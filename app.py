import os
from flask import Flask, render_template, request

app = Flask(__name__)

usuario_correto = "professor"
senha_correta = "1234"

fundamental = [
"6A","6B",
"7A","7B",
"8A","8B",
"9A","9B"
]

medio = [
"1M",
"2M",
"3M"
]


@app.route("/")
def login():
    return render_template("index.html")


@app.route("/entrar", methods=["POST"])
def entrar():

    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == usuario_correto and senha == senha_correta:
        return render_template("nivel.html")

    return "Usuário ou senha incorretos"


@app.route("/fundamental")
def tela_fundamental():
    return render_template("bimestre.html", nivel="fundamental")


@app.route("/medio")
def tela_medio():
    return render_template("bimestre.html", nivel="medio")


@app.route("/turmas/<nivel>/<bimestre>")
def turmas(nivel, bimestre):

    if nivel == "fundamental":
        lista = fundamental
    else:
        lista = medio

    return render_template(
        "turmas.html",
        turmas=lista,
        nivel=nivel,
        bimestre=bimestre
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)