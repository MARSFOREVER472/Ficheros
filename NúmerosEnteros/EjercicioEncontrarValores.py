# ESCRIBIR UNA FUNCIÓN QUE PIDA UN NÚMERO ENTERO ENTRE EL 1 Y EL 10, Y QUE LEA EL FICHERO CREADO POR "n" (tabla-n.txt) CON LA TABLA DE MULTIPLICAR DE ESE NÚMERO, EN DONDE "n" ES EL NÚMERO INTRODUCIDO, Y LA MUESTRE POR PANTALLA.
# SI EL FICHERO NO EXISTE DEBE MOSTRAR UN MENSAJE POR PANTALLA INFORMANDO DE ELLO.

n = int(input('INTRODUCE UN NÚMERO ENTERO DEL 1 AL 10: '))
name_fichero = 'tabla-' + str(n) + '.txt'

try:
    f = open(name_fichero, 'r')
except FileNotFoundError:
    print>('NO EXISTE EL FICHERO CON LA TABLA DEL', n)
else:
    print(f.read())
    f.close()