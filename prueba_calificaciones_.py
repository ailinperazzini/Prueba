# -*- coding: utf-8 -*-
"""Prueba-Calificaciones %.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1obIIPMLMlEIa0GG0IeCAT2cEewCzlo01
"""





"""DESAFIO CLASE 2 """

Nombre = input("Ingresar el nombre del Alumno   ")
Nota1 = float(input("ingresar primer nota    "))  #Nota 10- 15% del total
Nota2 = float(input("ingresar segunda nota   "))  #Nota 7 - 35% del total
Nota3 = float(input("ingresar tercer nota    "))  #Nota 4 - 50% del total
Nota_Final = round(Nota1*0.15+Nota2*0.35+Nota3*0.50)
print('La nota final de '+Nombre+' es', (Nota_Final))

"""Error en ultima linea: No me trae la nota con dato decimal"""

Nombre = input("Ingresar el nombre del Alumno   ")
Nota1 = float(input("ingresar primer nota    "))  #Nota 10- 15% del total
Nota2 = float(input("ingresar segunda nota   "))  #Nota 7 - 35% del total
Nota3 = float(input("ingresar tercer nota    "))  #Nota 4 - 50% del total
Nota_Final = (Nota1*0.15+Nota2*0.35+Nota3*0.50)
print("La nota final es de " + str(Nota_Final))

print(Nota_Final)

from google.colab import drive

drive.mount('/content/drive/')

!python "/content/drive/MyDrive/ejemplo_clases_coder.ipynb/prueba.py"