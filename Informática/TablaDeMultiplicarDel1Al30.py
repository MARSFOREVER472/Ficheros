# ESCRIBIR UNA FUNCIÓN QUE PIDA UN NÚMERO ENTERO ENTRE EL 21 Y EL 30 Y LO GUARDE EN UN FICHERO CON EL NOMBRE tabla-n.txt LA TABLA DE MULTIPLICAR DE ESE NÚMERO, EN DONDE "n" ES EL NÚMERO INTRODUCIDO POR LA CONSOLA.

n = int(input('INTRODUCE UN NÚMERO ENTERO ENTRE EL 21 Y EL 30: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')

for i in range(21, 30):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')

f.close()