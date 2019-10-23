from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Cursos')
def rounte():
    return render_template('cursos.html')

@app.route('/Detalhecurso')
def rounte1():
    return render_template('Detalhes.html')

@app.route('/Disciplina')
def rounte2():
    return render_template('Disciplina.html')

@app.route('/Noticias')
def rounte3():
    return render_template('Noticias.html')



app.run()