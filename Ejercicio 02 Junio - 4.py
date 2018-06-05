#! C:\Python27
# -*- coding: iso-8859-15 -*-

cantidad =int(input('Ingrese cantidad de articulos confort que va a comprar: '))
precio = int(input('Ingrese precio unitario de confort: '))

if cantidad > 10:
    descuento = precio * 0.25
    total = (cantidad * precio) - descuento
print('El precio a pagar es: ', total) 

elif cantidad >=5 and cantidad <= 9:
    descuento = precio * 0,2
    total = (cantidad * precio) - descuento
print('El precio a pagar es: ',total) 

else:
    cantidad <= 4
    descuento = precio * 0,15
    total = (cantidad * precio) - descuento
print('El precio a pagar es: ',total) 

