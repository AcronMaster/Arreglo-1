import time
from tabulate import tabulate

inicio_tiempo = time.time()
class calificaciones:

    def __init__(self):

        

        self.alumnos=[f"Alumno {i+1}" for i in range(100000)]
        self.materias=[f"Mareria {i+1}" for i in range(100)]

        self.matriz_calificaciones=[[f"calificacion {i+1}{j+1}" for j in range(len(self.materias))] for i in range(len(self.alumnos))]


    def mostrar_matriz(self, num_alumnos=100000):

        headers = ["Alumno"] + self.materias

        tabla=[[self.alumnos[i]] + self.matriz_calificaciones[i] for i in range(num_alumnos)]

        print(tabulate(tabla,headers,tablefmt="pipe"))
    
    def buscar_calificacion(self,alumno_num,materia_num):
         indice_alumno = alumno_num - 1  
         indice_materia = materia_num - 1

         if indice_alumno < len(self.alumnos) and indice_materia < len(self.materias):
            calificacion = self.matriz_calificaciones[indice_alumno][indice_materia]
            print(f"Calificación del {self.alumnos[indice_alumno]} en {self.materias[indice_materia]}: {calificacion}")
         else:
            print("El número de alumno o materia es inválido.")
 




datos=calificaciones()

datos.mostrar_matriz()

datos.buscar_calificacion(321, 5)

fin_tiempo= time.time()

tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
