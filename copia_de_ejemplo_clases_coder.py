# -*- coding: utf-8 -*-
"""Copia de ejemplo_clases_coder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/150QUKk9w5MgNramaWLi07xeqkxGXRr2H
"""

#Termino1                 
(34+6)*2

#pequeño ejemplo entre int y float
1.0+1

#ejemplo de procedencia
(((23 + 3.66)-6.66 )/ 4 ) ** 3

(5+2)*(7*8)

5+2*7*8

type('Gabo es!&$ un2312 profe horrible :(')

#ejemplo de print con un buleano
type(1.2)

print(r'C:Gabo\nuevo\otronuevo')

solicitud_edad = int(input('decime tu edad'))

type(solicitud_edad)

palabra = "Pithon"

len(palabra)

print(palabra[0:1], palabra[2:])

palabra2 = palabra[0:2]

palabra = palabra[0:1] + 'y' + palabra[2:]

nota = float(input("ingresa la nota"))

palabra

"""**Listas** y **tuplas**"""

lista1 = [1, 12, 123]

lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append("Hola")

lista1

lista3 = lista1

lista3.pop(-1)

lista5 = lista1 + lista2

lista5

lista3

lista = [1,2,1,3,4,1]

lista.index(1)

lista.pop(-1)

lista

lista

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

print(tupla[-1])

print(len(tupla))

print(tupla.index(87), tupla[9])

lista_nueva = list(tupla[-3:]) 
print(lista_nueva)

print(tupla[8], tupla.index(-783))

print(tupla.count(7))

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
tupla[-3:]

"""Ejemplos de asignaciones lógicas!!"""

False == True

10 >= 2*4

33/3 == 11

True > False

True*5 == 2.5*2

not False

not False

33/3 == 11 and 5 > 2

False or False

True*5 == 2.5*2 or 123 >= 23

12 > 7 and True < False

expresiones = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]

exp2 = expresiones

exp2

expresiones = [False == True,10 >= 2*4,33/3 == 11,True > False,True*5 == 2.5*2]

type(expresiones)

expresiones2 = expresiones

expresiones2

nombre = input("su nombre")

edad = int(input("su edad"))

edad += 30

nombre != "****" and len(nombre) >= 3 and len(nombre) < 10

edad > 10 and edad < 18 and edad * 4 > 40

len(nombre) >= 3 and len(nombre) < 10

edad * 4 > 40

a = 1
a += 1
a += 3
a -= 5
a

a = 30

a = a + 1
a = a + 3
a = a - 5

a

c = 15.2

c == str

"""**Ejemplos sobre if**"""

edad = int(input("edad"))

if edad > 80:
  
  print(f"tu edad es {edad}", edad)

  print(f"tu edad es {edad}")

if edad == 71:
  import this

a = 5
b = 10

if a==2 and b == 10:

  print(a , b)

else:
  
  print("ninguno cumple la condición")

tu_edad = input(" ingresa tu edad ")

#acá comiensza el filtrado para reconocer si nos están poniendo un caracter vacio
if tu_edad == "":
  
  tu_edad = input(" ingresa nuevamente edad ")

#si es así nos va a volver a pedir que ingresemos la edad.
edad_transformada = int(tu_edad)

#una vez ingresada la edad entonces las transformammos a entero para que pueda averiguar si es menor o mayor
print(edad_transformada)

if edad_transformada >= 18:
  print("bienvenido")
else:
  print("sos un purrete ")

nombre = input("¿Cómo te llamas? ")

genero = input("¿Cuál es tu preferencia (M o C)? ")

if genero == "M":
  if nombre < "m":
       grupo = "A"
  else:
       grupo = "B"
else:
   if nombre > "n":
       grupo = "A"
   else:
       grupo = "B"
print("Tu grupo es " + grupo)

"a" > "b"

"""**ITEREMOS**"""

edad = input("tu edad")

while edad == "":
  edad = input("tu edad")

print(edad)

num = 5
while num >= 0:
  print(f'{num}')
  num -= 1 # num = num - 1 
print('Terminó el conteo!')

numero = int(input("ingrese su número"))

contador = 0

while numero != 0:
   contador = contador + numero
   
   print(f"Tu numero vale: {numero}\n")

   numero = int (input("Ingresar otro numero, 0 para salir\n"))
   
      
else:
  print(f"Has salido con una suma de : {contador}")

n = 5
while n < 10:
    n -= 1
    
    if n == 2:
      print("ahora que n vale 2 salimos")
      break
      
    print("n vale ", n)

n = 0

while n < 10:
  n += 1
  if n == 2:
    print("Continuamos con la siguiente iteración")
    continue  #termina o ignora esa rep...!!!
    #Continuar con la siguiente iteración 

  print("n vale ", n)

n = 0

while n < 10:
  n += 1
  if n == 2:
    pass
    
  print("n vale ", n)

lista = [0,1,2,3,5]

for empanada in lista:
  print(empanada)

#         0  1  2  3  
lista = [66,-3,35,96]
#---Pos ,   elem
for indice, numero in enumerate(lista):

  print(f"INDICE: {indice}")
  print(f"NUMERO: {numero}\n\n")

  print(f"------> {lista[indice]}\n\n----------------")

for numero in range(10):  #desde 0 hasta  < "10"
 
  print(f"----> {numero}")

for numero in range(2,10,2):  #arranca en 2, termina en 9... va de 2

  print(f"----> {numero}")

paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']

for indice, pais in enumerate(paises):
  print(f"el numero de {pais} es {indice}")

n = 0
for i in range(101):
  
  if (i % 2) == 0:
   n = n + i

print(n)

a = 11

while a > 0:
  a -= 1
  print(a)

for i in range(10, 0, -1):
  print(i)

peticion = input("por favor ingrese un numero de mas de 3 digitos ")

devolucion = len(peticion)

print(f"su numero tiene {devolucion} digitos" )

"""**Conjuntos**"""

conjunto1 = {1,2,"Gabi", "Gabo"}

for i in conjunto1:
  print(i)

list(conjunto1)

set(conjunto1)

conjunto1.add("Nadia :)")

conjunto1.update([33,12, "Juan"])

conjunto1

conjunto1.discard(33)

conjunto1.remove("Pepe")

conjunto1.pop()

conjunto1

"""**practiquemos**"""

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

grupo2 = {"Ana", "Ramón", "Marta", "Eric", "David" }

for item in grupo2:
  grupo.add(item)

grupo

for eliminado in grupo:

  if eliminado == "Mario" or eliminado == "Miguel" or eliminado == "Esteban":
    grupo.discard(eliminado)

grupo





animales={"elefante":""}

animales["casuario"] = "Brad"

"""animales.update({"perro":"tuky", "tigre":"Tony","mono":"Burgos"})"""

animales.update({"perro":"tuky", "tigre":"Tony","mono":"Burgos"})

animales

animales["elefante"] = "Trompita"

animales

animales.update({"elefante":"Dumbo", "Delfín":"Octavio"})

animales

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

texto[:21]

texto1 = texto[:21] + "..."

print(texto1 , texto)

lineas = texto.split("&")

for i, linea in enumerate(lineas):
   
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " + lineas[i] + "."

# Mostramos el texto final
for linea in lineas:
   
   print(linea)

lista_desafio = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

conjunto = set(lista_desafio)

lista_desafio = list(conjunto)

lista_desafio

lista_desafio.sort(reverse=True)

lista_desafio

for i in lista_desafio:
  if (i%2 == 1):
    lista_desafio.remove(i)

lista_desafio

lista_sumada = sum(lista_desafio)
print(lista_sumada)

#                  index valor
lista_desafio.insert(0 , lista_sumada)
print(lista_desafio)

print(lista_desafio[0] == sum(lista_desafio[1:]) )

from google.colab import drive
drive.mount('/drive/')

ruta = '/drive/MyDrive/ejemplo' # cd drive/mydrive

ruta

f = open(ruta + "/archivo.txt", "w")

f.write("Esto es otro texto, y así escribo TXT con Python")

f.close()

nombre = "Gabriel"
apellido = "Rumani"
dni = 111111

d = {"NOMBRE":nombre, "APELLIDO":apellido, "DNI":dni}

f = open(ruta + "/otro.txt", "w")

f.write(d["NOMBRE"] +"," +d["APELLIDO"] +"," +str(d["DNI"]))

f.close()

f = open(ruta + "/otro.txt", "r")
content = f.read()
print(content)
f.close()

"""**La mascota**"""



nombre_mascota = input("como se llama tu mascota? ")

edad_mascota = input("cuantos años tiene? ")

guardar_dato_mascota = open(ruta + "/miMascota.txt", "w")

dato_mascota = f"mi mascota se llama {nombre_mascota} y tiene {edad_mascota} años"
#toma un argumento!!!
guardar_dato_mascota.write(dato_mascota)

guardar_dato_mascota.close()

j = open(ruta + "/lorem.txt", "w")

r = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages"

j.write(str(r))

f = open(ruta + "/lorem.txt", "r")

for line in f.readlines():
    print(line)


f.close()

f = open(ruta + "/lorem.txt", "r")

print(f.readline())


f.close()

f = open(ruta + "/ejemplo_vivo.txt", "w")

f.write("Hola Julián")

f.close()

from os import remove

remove(ruta + "/otro.txt")

f = open(ruta + "/lorem.txt", "r")

f.seek(100)

print(f.read())


f.close()

import json  #Importar las funciones de json en la 
#clase 15 entenderemos mejor el IMPORT

data = {}

data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open(ruta + "/primerJson.json", 'w') as file:
    json.dump(data, file, indent=4)

dataLectura['clients']

with open(ruta + "/primerJson.json") as file:

    dataLectura = json.load(file)

    for client in dataLectura['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')

#Con esto daremos permisos para acceder al Drive, nos va a pedir que hagamos loguin con la cuenta de gmail, y nos dará un codigo de verificación. 

from google.colab import drive

#Para generar una variable con los datos de nuestro archivos, vamos a empezar a trabajar con nuestra libreria "magica" para trabajar con datos, 
#libreria llamada Pandas, para poder usarla debemos hacer lo siguiente

import pandas as pd  #En castellano, importamos pandas y lo llamamos pd  (pd puede ser cualquier palabra que recuerden)

import numpy as np #Esto lo usaremos bastante mas adelante del apunte, por ahora se lo puede ignorar

#En mi caso voy a abrir los datos de turnos de vacunación por covid-19

variableTurnos = pd.read_csv(ruta+ "/dataset_turnos_detalle.csv")

#Acá se vé que era necesario tener pandas, ya que usamos la función read_csv de pandas.
#LISTO... Ya tenemos todos nuestros datos leidos y guardados en una variable... Ya son "facilmente" manipulables.

variableTurnos

#Si esa visualización por defecto no nos gusta podemos verlos de otra forma. Head, nos permite elegir cuantos datos mostrar
variableTurnos.head(50) #Los primeros

#Con el comando tails, agarramos los ultimos
variableTurnos.tail(40)

#Tambien podemos usar sample, que nos muestra la cantidad que quieras, pero al azar, bastante util. 
variableTurnos.sample(50)

variableTurnos["sede"]

#Uno de los primeros estadisticos para entrar en tema podría ser las frecuencias simples..
variableTurnos['genero'].value_counts()  #Esto nos muestra cada sede una vez sola, ordenado y con su frecuencia.

"""**Nuestras primeras funciones**"""

#Mi primer función

def funcion_saludar():

  print("Hola Coder")
  print("----------")
  print("primera función")

funcion_saludar()

def funcion_saludar_nombre(): #nombre es mi parametro de entrada
  nombre = "Eze" #variable local
  print("Hola Coder")
  print("----------")
  print(f"El mejor es: {nombre}")

un_nombre = input("ingrese un nombre ")#global

funcion_saludar_nombre()  #Le envio un nombre

nombre  #No funciona porque vive solo en la funcion, variable Local :)

variable_test = 10  #Vive en todo mi colabs --- Variable global

def test():
  
  print(f"{variable_test}")

test()

variable_test

#Las funciones anteriores .... "Procedimientos"
def saludo_nombre(nombre):
  print("estamos acá")
  saludo = f"Hasta pronto, {nombre} gracias por venir!!!"
  print("ahora estamos acá")
  return saludo

pepa = saludo_nombre("Pepa")

pepa

#Procedimiento
def suma1 (a, b):
  resultado = a + b
  print(f"El resultado de la suma es: {resultado}")

suma1(11, 9)

variable = suma1(11,9)  #variable <------ 20

variable

#Forma A
var1 = suma1(5,1)

var1

#Forma B
print(f"{suma1(519,111)}")

#Mostrar los numeros entre -11 y 108 que no sean divisibles por 3

def numeros_entre_no_divisibles(desde, hasta, noDivisible ):

        for x in range(desde, hasta):

          if ( not (x % noDivisible == 0) ):


            print(f"Este numero no es divisible por {noDivisible}: {x}")

numeros_entre_no_divisibles(-1001, 3, 2)  #10 11 13 14 15 17 18 ...

def es_par(numero):

  #Recordar type()

  if ( type(numero) == int):

        if ( numero % 2 == 0):

          print("PAR")

        else: 
          
          print("IMPAR")

  else: 

        print("ERROR, mandame un entero")

def resta(a = None,b = None):
  
  return a - b

resultado = resta()

def cuenta(numero):

  numero -=1

  if numero >0: 

    cuenta(numero)
    print(f"---->{numero}")

cuenta(11)

def sumar(numero):
  numero *= 2
  return numero

nuevo_numero = sumar(9)

nuevo_numero

def suma(*args):
  s = 0
  for arg in args:
    s += arg
  return s

ej1 = suma(1,2)

ej1

def sumas(**kwargs):
  s = 0
  for key, value in kwargs.items():
    print(key, "=" , value)
    s += value
  return s

sumas(a=2, b=3, c=4, pizza = 5 , aguila = 6)

def calcular_horas(segundos):

  minutos = segundos // 60 #sin resto
  segundos_resto = segundos % 60

  horas = minutos // 60
  minutos_resto = minutos % 60

  return horas, minutos_resto, segundos_resto

muestra = calcular_horas(5430) #1 hora y media
muestra

def calcular_segundos(hora, minuto, segundo):
  
  hora = hora *60 *60
  minuto = minuto *60 

  segundo += hora
  segundo += minuto
  return segundo

muestra2 = calcular_segundos(1,30,30)

muestra2

def calcular(*args):
	if len(args)==1:
		return calcular_horas(args[0])
	elif len(args)==3:
		return calcular_segundos(*args)
	else:
		raise TypeError("Se espera 1 o 3 parámetros")

calcular(5490)

"""**Conociendo nuestros errores**

"""

n  = input("ingrese n ")

m = 4

print(f"{n}/{m} = {n/m}")

n = float(input("ingrese n "))

m =  4

print("{}/{} = {}".format( "hola", "hola de nuevo", 5+5 )) #veamos un poco más del format

4 / 0

def dividir(a, b):
  if b == 0:
    return "no se puede dividir por cero"
  return a/b

ejemplo = dividir(4,8)

ejemplo

try:
      n = float(input("Ingresar n:\n") ) #input dan una cadena

      m = 4

      print(f"---> {n}/{m} = {n/m}")
except:

    print("Algo salio!!!! :( ")

while (True):
  try:

      n = float(input("Ingresar n:\n") ) #input dan una cadena

      m = 4

      print(f"---> {n}/{m} = {n/m}")
      break
  except:

    print("Algo salio!!!! :( ")

while (True):
  try:

      n = float(input("Ingresar n:\n") ) #input dan una cadena

      m = 4

      print(f"---> {n}/{m} = {n/m}")
      
  except:

    print("Algo salio!!!! :( ")
  
  else:
    break

    print("todo bien")
    print("por fin pusiste un número y te dejaste de hacer el gracioso")

while(True):
    #TRY es obligatorio y except
    try:
      nombre = input("Ingresar su nombre\n")

      n = float(input("Ingresar un n\n"))

    except:
      print("Estas loco no puedo castear esto!!!!")

    #BLOQUE OPCIONAL
    else:  #else se ejecuta cuando no entraste al except

      print("Todo salio bien, gracias")
      break

    #BLOQUE OPCIONAL
    finally:

      print(f"Gracias por estar presente {nombre}")

try:
  n = input("introduce un número: ")
  5/n
except Exception as e:
  print("error", type(e).__name__)

print(type(True).__name__)

try:
  n = float(input("introduce un número "))
  5/n
except TypeError:
  print("no se divide una cadena")
except ValueError:
  print("introduce un número por favor")
except ZeroDivisionError:
  print("no se puede dividir por cero")
except Exception as e:
  print("error ", type(e).__name__)
else:
  print("por fin")

def dividir(a, b):
  try:
    return a/b
  except ZeroDivisionError:
    print("no se puede dividir en cero")

dividir(2,2)

lista1 = [["ola", "chau", "adis", "otro saludo"],["hola", "chau", "adios", "otro saludo"]]
lista1

item = []

for i in lista1:
  
  if "ola" in i:
    item.append(i)

nuevo_item = tuple(item[0])
    # lista1.insert(0,i)
for i in lista1:
  if "ola" in i:
    i[0] = "aló"
  # if "adis" in i:
  #   nuevo_item[0][1]="bye"
  #   lista1.append(nuevo_item)
# nuevo_item[0][1]="bye"
# lista1.append(nuevo_item)

print(lista1, nuevo_item)

"""**Empecemos con las clases!!!**"""



#definimos la primera clase
class Perro: 
  pass

perro1 = Perro()
perro2 = Perro()

#De esta forma se crean dos perros. Tienen las mismas caracteristicas pero son distintos

class Perro: 
  #El constructor
  def __init__(self, nombre, raza):

    #Atributos de instancia
    self.nombre = nombre
    self.raza = raza

class Perro: 
  #atributos de clase
  especie = "Mamífero"

  #El constructor
  def __init__(self, nombre, raza):
    self.nombre = nombre
    self.raza = raza
    

    #Atributos de instancia
    # self.nombre = nombre
    # self.raza = raza

perro1 = Perro("Sammy", "Caniche")

print(f"Así se ve el objeto: {perro1}  <---  :( Feo por ahora")  

print(f"Mejor verlo atribto por atributo {perro1.nombre}, {perro1.raza}, {perro1.especie}")



class Perro: 
  #atributos de clase
  especie = "Mamifero"

  #El constructor
  def __init__(self, nombre, raza):
    print(f"{nombre},{raza}")
    #Atributos de instancia
    self.nombre = nombre
    self.raza = raza

  #Método sin argumentos
  def ladrar(self):
    print("Este perro acaba de ladrar")
  #Método con argumentos
  def caminar(self, pasos):
    print(f"Este perro acaba de caminar {pasos} pasos")

perro1 = Perro("Bobby", "Salchicha")

perro1.caminar(8)
perro1.ladrar()

print(perro1)

"""**Esa es la definición por defecto del método str, por suerte podemos modificarlo a nuestro gusto:**"""

class Persona:
  especie = "humano"
  corazon = 1
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def saludar(self):
    print("hola Señor Tomson")

  def trotar(self, km):
    print(f"hoy pude correr {km} kilómetros")

Gabo = Persona("Gabriel", "Rumani", 24)

print(Gabo.nombre, Gabo.apellido, Gabo.edad, Gabo.especie, Gabo.corazon)
Gabo.saludar()
Gabo.trotar(200)

"""class Perro: 
  #atributos de clase
  especie = "Mamifero"

  #El constructor
  def __init__(self, nombre, raza):

    #Atributos de instancia
    self.nombre = nombre
    self.raza = raza

  #Método especial __str__
  def __str__(self):
    return "\nNombre:" +self.nombre +",  Raza:" +self.raza +",  Especie:" +self.especie

  #Método sin argumentos
  def ladrar(self):
    print("Este perro acaba de ladrar")
  #Método con argumentos
  def caminar(self, pasos):
    print(f"Este perro acaba de caminar {pasos} pasos")
"""

class Vector():
    def __init__(self, data):
        self._data = data
        
    def __str__(self):
        return f"The values are: {self._data}"
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, pos):
        return self._data[pos]
    
    def __setitem__(self, pos, value):
        self._data[pos] = value
    
    def __iter__(self):
        for pos in range(0, len(self._data)):
            yield f"Value[{pos}]: {self._data[pos]}"
            
v = Vector([1,2,3])
print(v)
print(len(v))
print(v[0])
v[1]=20
print(v)
for vec in v:
    print(vec)

perro1 = Perro("Bobby", "Dalmata")

print(f"{perro1}")

class Persona: 

    def __init__(self, nombre, apellido, perro):
        self.nombre = nombre
        self.apellido = apellido
        self.perro = perro


    def __str__(self):
        return "Mi nombre es: " +self.nombre +" " +self.apellido +"\n" +self.perro.__str__()

persona1 = Persona("Gabo", "Perez", perro1)

print(persona1.nombre, persona1.perro.nombre, persona1.perro.raza)

class Sueldo:

    def __init__(self, sueldo):
        self.sueldo = sueldo

    def __str__(self):
        return f"\nSUELDO: {self.sueldo}"


class Empleado:

    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = Sueldo(1200)


    def __str__(self):
        return f"NOMBRE: {self.nombre}\nPUESTO: {self.puesto}\n" +self.sueldo.__str__()

s1 = Sueldo(200)
emp1 = Empleado("Nico", "Profe")

print(f"RESULTADO 1:  {s1}\n")
print(f"RESULTADO 2:  {emp1}")

class Persona:

    tipo = "Humano"  #Dato al que pueden acceder
    __sueldo = 2000  #No quiero que accedan a mi cuenta 

    def __init__(self, nombre, apellido):
        self.nombre = nombre  #NO me molesta que sepan mi nombre
        self.__apellido = apellido #No quiero que sepan mi apellido

    def edad(self):
        return 31 #Soy joven aún no miento con mi edad



persona1 = Persona("Gabo", "Rumo")

print(f"Resultado1: {persona1.tipo}\n")
#print(f"Resultado2: {persona1.__sueldo}\n")
print(f"Resultado3: {persona1.nombre}\n")
#print(f"Resultado4: {persona1.__apellido}\n")
#print(f"Resultado5: {persona1.__soy_feliz()}\n")
print(f"Resultado6: {persona1.edad()}\n")



class Jugador:
    
    def __init__(self, nombre, apellido):

        #Se suelen hacer privados todos los atributos
         self.__nombre = nombre
         self.__apellido = apellido
         self._goles = 23   #Un solo guion bajo no es ni publico ni privado, es protegido, que en la proxima clase lo entenderemos

    #Se generan metodos get PUBLICOS de los atributos que quieres que sean visibles.
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    #Se generan metodos set PUBLICOS de los atributos que quieres que sean visibles y MODIFICABLES
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

        
jugador1 = Jugador("Brenda", "Benitez")
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre()
jugador1.set_apellido("Gutierrez")  #Para modificar al apellido
jugador1.set_nombre("Ricardo")  #Para acceder al nombre
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre
print(jugador1._goles)  #qué pasa con los goles

#Nuestro atleta

class Atleta:
  def __init__(self, nombre, apellido, altura, peso, telefono):
    self.nombre = nombre
    self.__apellido = apellido
    self.altura = altura
    self.peso = peso
    self.__teleono = telefono

  def get_nombre(self):
    return self.nombre

  def set_nombre(self,nombre):
     self.nombre = nombre

  def masa_corporal(self, peso, altura):
    indice = float(peso/altura**2)
    print(f"tu masa corporal es {indice}")

ali=Atleta("Mohamed","Ali", 1.91, 100, "0606456")

# ali.masa_corporal(ali.peso, ali.altura)
print(ali.get_nombre())
ali.set_nombre("Casius")
print(ali.get_nombre())