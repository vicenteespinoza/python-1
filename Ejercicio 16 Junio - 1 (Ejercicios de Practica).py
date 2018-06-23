#! C:\Python27
# -*- coding: iso-8859-15 -*-

#Escribir un programa que pregunte al usuario su nombre y apellido, imprima un mensaje saludándolo.

nombre =str(raw_input('Ingrese su nombre: '))
apellido = str(raw_input('Ingrese su apellido: '))
nombre_completo = nombre+" "+apellido
print('Buenos dias ',nombre_completo)