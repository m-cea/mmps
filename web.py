from flask import Flask
from flask import render_template
from flask import Response

app = Flask(__name__)

@app.route('/AlgoContigo')
def AlgoContigo():
    return render_template("Algo Contigo.html")

@app.route('/AyAmor')
def AyAmor(): 
    return render_template("Ay Amor.html")

@app.route('/ComoTodaMujer')
def ComoTodaMujer():
    return render_template("Como Toda Mujer.html")

@app.route('/DileQueVuelva')
def DileQueVuelva():
    return render_template("Dile que vuelva.html")

@app.route('/HayQueSalvarNuestroAmor')
def HayQueSalvarNuestroAmor():
    return render_template("Hay que salvar nuestro amor.html")

@app.route('/LaTerceraEsLaVencida')
def LaTerceraEsLaVencida():
    return render_template("La tercera es la vencida.html")

@app.route('/PielCanela')
def PielCanela():
    return render_template("Piel Canela.html")

@app.route('/QuienSoy')
def QuienSoy():
    return render_template("Quien soy.html")

@app.route('/SieteNotasDeAmor')
def SieteNotasDeAmor():
    return render_template("Siete notas de amor.html")

@app.route('/VoyAPerderLaCabezaPorTuAmor')
def VoyAPerderLaCabezaPorTuAmor():
    return render_template("Voy a perder la cabeza por tu amor.html")

if __name__ == '__main__':    
    app.run(host='0.0.0.0')
