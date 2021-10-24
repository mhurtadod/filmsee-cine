from typing import List
from flask import Flask
from flask import render_template
from flask import request

import sys
from model.Pelicula import Pelicula

from connection.Connect import sql_insert_pelicula, sql_select_peliculas
app= Flask (__name__)

#www.google.com/
#Datos en memoria
listadoPeliculas = list[Pelicula]()
esAdmin = True #se debe ajustar para que este valor sea dinamico segun la información que retorne el servicio de autenticacion(login)

@app.route('/cartelera/')
def get_cartelera():
    peliculas = sql_select_peliculas()
    return render_template("peliculas.html", peliculas=peliculas, esAdmin = esAdmin)




@app.route('/cartelera/', methods = ["POST"])
def create_cartelera():

    nuevaPelicula: Pelicula = Pelicula( nombre= request.form['nombre'],
                                        portada = request.form['portada'],
                                        anio = request.form['anio'])
    global listadoPeliculas
    sql_insert_pelicula(nuevaPelicula)
    print('create_peliculas:' + str(len(listadoPeliculas)), file=sys.stderr)
    return get_cartelera()


