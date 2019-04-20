from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/play')
def juego():
    return render_template('juego.html')

@app.route('/normas')
def normas():
    return render_template('normas.html')

@app.route('/help')
def ayuda():
    return render_template('ayuda.html')

if __name__ == '__main__':
    app.run(debug=True)