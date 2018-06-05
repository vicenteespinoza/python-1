#! C:\Python27
# -*- coding: iso-8859-15 -*-

n = int(input('Ingrese la cantidad de cauchos a comprar: '))
p = float(input('Ingrese el precio unitario: '))
if n >= 6:
    desc = 0.15 * p
    total = p - desc
else:
    desc = 0.1 * p
    total = p - desc
suma=n*total
print('El total a pagar es: ' ,suma)