import os
from flask import Flask, render_template, request

app = Flask(__name__)

usuario_correto = "professor"
senha_correta = "1234"

fundamental = [
"6º A","6º B",
"7º A","7º B",
"8º A","8º B",
"9º A","9º B"
]

medio = [
"1º Ano",
"2º Ano",
"3º Ano"
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

    return "<h2>Usuário ou senha incorretos</h2>"


@app.route("/fundamental")
def fundamental_nivel():
    return render_template("bimestre.html", nivel="fundamental")


@app.route("/medio")
def medio_nivel():
    return render_template("bimestre.html", nivel="medio")


@app.route("/turmas/<nivel>/<bimestre>")
def turmas(nivel, bimestre):

    if nivel == "fundamental":
        turmas_lista = fundamental
    else:
        turmas_lista = medio

    return render_template(
        "turmas.html",
        turmas=turmas_lista,
        bimestre=bimestre,
        nivel=nivel
    )


# evitar erro no render
@app.errorhandler(500)
def erro500(e):
    return "<h2>Erro interno do servidor</h2><p>Verifique os templates.</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
