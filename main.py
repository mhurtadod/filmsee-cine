from typing import List
from flask import Flask
from flask import render_template
from flask import request;
from model.Pelicula import Pelicula
import sys
app= Flask (__name__)

#www.google.com/
#Datos en memoria
listadoPeliculas = []
esAdmin = True #se debe ajustar para que este valor sea dinamico segun la información que retorne el servicio de autenticacion(login)

@app.route('/cartelera/')
def get_cartelera():
    print('get_peliculas:' + str(len(listadoPeliculas)), file=sys.stderr)
    if len(listadoPeliculas) == 0:
    
        listadoPeliculas.append(Pelicula("Venon", "https://archivos-cms.cinecolombia.com/images/_aliases/exhibition_poster/3/4/1/1/21143-1-esl-CO/VNM2-2-Poster.png", 2021))
        listadoPeliculas.append(Pelicula("Sin tiempo para morir", "https://archivos-cms.cinecolombia.com/images/_aliases/exhibition_poster/5/0/8/2/12805-29-esl-CO/BOND_Cineco_2-Poster_480x670.jpg", 2021))
        listadoPeliculas.append(Pelicula("Shang - Chi", "https://archivos-cms.cinecolombia.com/images/_aliases/exhibition_poster/8/2/0/0/20028-1-esl-CO/02_STB_P143_Ringfight_ARG.jpg", 2021))

    return render_template("peliculas.html", peliculas=listadoPeliculas, esAdmin = esAdmin)




@app.route('/cartelera/', methods = ["POST"])
def create_cartelera():

    nuevaPelicula: Pelicula = Pelicula( nombre= request.form['nombre'],
                                        portada = request.form['portada'],
                                        anio = request.form['anio'])
    global listadoPeliculas
    listadoPeliculas.append(nuevaPelicula)
    print('create_peliculas:' + str(len(listadoPeliculas)), file=sys.stderr)
    return get_cartelera()


