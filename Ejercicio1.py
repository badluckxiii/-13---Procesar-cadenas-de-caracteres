#   Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco
#  se ingresaron. Tener en cuenta que un espacio en blanco es igual a " ",
#  en cambio una cadena vacía es ""
string='Tres tristes tigres comen trigo en un trigal'
espacios=0
for x in string:
    if(x==' '):
        espacios+=1
print('Número de espacios ',espacios)