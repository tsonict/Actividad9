from particula import Particula

class Particulas:
    def __init__(self):
        self.__list_particulas = []

    def agregar_final(self, particula:Particula):
        self.__list_particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__list_particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__list_particulas:
            print(particula)

p01 = Particula(id=123, origen_x= 20, origen_y= 25, destino_x= 70, destino_y= 30, velocidad= 14123, red= 10, green= 255, blue= 255)


particulas = Particulas()

particulas.agregar_final(p01)
particulas.mostrar()