from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Cursos')
def rounte():
    return render_template('cursos.html')



app.run()