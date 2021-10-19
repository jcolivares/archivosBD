#!/usr/bin/env python
# Script para leer archivos

#Se abre el archivo para lectura
archivo = open("README.md", 'r')

#El método read lee todo el documento asalvo que sea muy grande el archivo
mensaje = archivo.read()

print(mensaje)