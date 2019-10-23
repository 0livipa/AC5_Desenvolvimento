from flask import Flask, render_template
app = Flask(__name__)
#Leonardo - Atualizando página da home
@app.route('/')
def index():
    return render_template('Index.html')
#Renata - Atualizando página de cursos
@app.route('/Cursos')
def rounte():
    return render_template('cursos.html')

#Suelen - Atualizando página de detalhes
@app.route('/Detalhecurso')
def rounte1():
    return render_template('Detalhes.html')
#Felipe - Atualizando página de disciplina
@app.route('/Disciplina')
def rounte2():
    return render_template('Disciplina.html')

app.run()
