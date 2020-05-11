# Solicitar el ingreso de una clave por teclado y almacenarla en una cadena
# de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres 
# para que sea válido, en caso contrario mostrar un mensaje de error. 
x=' '
while len(x)<10 or len(x)>20:
    x=input('Cadena:\n')
    if(len(x)<10 or len(x)>20):
        print('Tienes que tener mas de 10 caracteres o menos de 20 caracteres')
