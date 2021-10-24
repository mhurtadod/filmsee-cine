import os
from flask import Flask, flash, render_template, request, jsonify
import sqlite3
from sqlite3 import Error

from model.Pelicula import Pelicula

app = Flask(__name__)
app.secret_key = os.urandom(24)


def sql_connection():
    try:
        conn = sqlite3.connect('bd/FilmSee.db')
        print('¡Conexión OK!')
        return conn
    except Error:
        print(Error)

def sql_select_peliculas():
    sql = "SELECT id, nombre, portada, anio FROM Peliculas"
    print(sql)
    conn = sql_connection()
    cursoObj = conn.cursor()
    cursoObj.execute(sql)
    peliculas = cursoObj.fetchall()
    #[ (47, 'Monitor', 368000.0, 23), (99, 'Mouse', 25000.0, 64), (104, 'Teclado', 48000.0, 77) ]
    lista_productos = [ Pelicula( pelicula[1], pelicula[2], pelicula[3]) for pelicula in peliculas ]
    return lista_productos

def sql_insert_pelicula(pelicula: Pelicula):
    sql = "INSERT INTO Peliculas (nombre, portada, anio) VALUES ('{}','{}','{}')".format(pelicula.nombre, pelicula.portada, pelicula.anio)
    print(sql)
    conn = sql_connection()
    cursoObj = conn.cursor()
    cursoObj.execute(sql)    
    conn.commit()
    conn.close()    

def sql_edit_pelicula(id, nombre, portada, anio):
    sql = "UPDATE Peliculas SET nombre = '{}', portada = '{}', anio = '{}' WHERE id = '{}'".format(nombre, portada, anio, id)
    print(sql)
    conn = sql_connection()
    cursoObj = conn.cursor()
    cursoObj.execute(sql)    
    conn.commit()
    conn.close()    

def sql_delete_pelicula(id):
    sql = "DELETE FROM Peliculas WHERE id = '{}'".format(id)
    print(sql)
    conn = sql_connection()
    cursoObj = conn.cursor()
    cursoObj.execute(sql)    
    conn.commit()
    conn.close()  
