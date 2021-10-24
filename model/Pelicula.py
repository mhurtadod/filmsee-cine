class Pelicula:
    id: str
    nombre: str
    portada: str
    descripcion: str
    anio: int
    def __init__(self, nombre, portada, anio):
        self.nombre = nombre
        self.portada = portada
        self.anio = anio