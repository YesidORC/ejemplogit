print("Hola Mundo")

class Paciente:
    def __init__(self):
        self.__name = "" 
        self._cc = 0

    def __str__(self):
        return f"Nombre: {self.__name}"