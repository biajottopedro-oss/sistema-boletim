import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

usuario_correto = "professor"
senha_correta = "1234"

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/entrar", methods=["POST"])
def entrar():

    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == usuario_correto and senha == senha_correta:
        return render_template("painel.html")
    else:
        return "<h2>Usuário ou senha incorretos</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)