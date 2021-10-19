#!/usr/bin/python
# Script para leer archivos

#Se abre el archivo para lectura
archivo = open("README.md", 'r')

#El método read lee todo el documento asalvo que sea muy grande el archivo
mensaje = archivo.read()

print("Archivo completo=", mensaje)

#Debemos cerrar el archivo y volverlo abrir para empezar el puntero de archivo desde el inicio
archivo.close()

#Se vuelve a abrir
archivo = open("README.md", 'r')

#Se puede leer por linea por línea utilizando el método readline()
mensaje = archivo.readline()
print("Leer una línea", mensaje)

#utilizando el método readlines() obtiene todo el archivo por línea

mensaje=archivo.readlines()
print("Con el método readlines==", mensaje)

print("Mensaje linea por linea:")
for linea in mensaje:
    print(linea, end="")

archivo.seek(0)

print("\n------>Usando la misma interaccion")
for linea in archivo:
    print(linea)

