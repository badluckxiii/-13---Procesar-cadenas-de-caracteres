#  Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
#  Contar la cantidad de vocales. Crear un segundo string con toda la oración en
#  minúsculas para que sea más fácil disponer la condición que verifica que es una
#  vocal. 
string='Lorem ipsum dolor sit amet, consectetur adipiscing elit. In lacinia' 
'fringilla dui, in euismod tortor ullamcorper at. In quis ultricies purus, ut' 
'elementum erat. Aliquam erat volutpat. Pellentesque at nisi eu libero pulvinar r'
'utrum et'
vocal=0
for x in string:
    if(x=='a' or x=='A'or x=='e'or x=='E'or x=='i'or x=='I' or x=='o'or x=='O'
    or x=='u' or x=='U'):
        vocal+=1
print('Número de vocales:',vocal)

