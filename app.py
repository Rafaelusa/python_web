from flask import Flask, render_template

app = Flask(__name__)

#Posts Mock
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Meu segundo Post"
    },
    {
        "titulo": "Post 3",
        "texto": "Novo Post"
    }
]

@app.route('/')
def exibir_entradas():
    
    return render_template("exibir_entradas.html", entradas=posts)
