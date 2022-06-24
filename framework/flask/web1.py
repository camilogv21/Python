from pydoc import render_doc
from flask import Flask

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    diccionario = {
        "nombre" : "",
        "apellido" : "",
        "edad" : 0
    }
    
    print ("-"*30)
    n = input("digite tu nombre: ")
    a = input("digite tu apellido: ")
    e = int(input("digite tu edad: "))
    
    diccionario["nombre"] = n
    diccionario["apellido"] = a
    diccionario["edad"] = e
    
    print(diccionario)
    print("-"*30)
    return render_template('index.html',value = diccionario)