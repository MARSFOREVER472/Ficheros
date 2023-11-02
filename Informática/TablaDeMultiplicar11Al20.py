# ESCRIBIR UNA FUNCIÓN QUE PIDA UN NÚMERO ENTERO ENTRE EL 1 Y EL 10 Y LO GUARDE EN UN FICHERO CON EL NOMBRE tabla-n.txt LA TABLA DE MULTIPLICAR DE ESE NÚMERO, EN DONDE "n" ES EL NÚMERO INTRODUCIDO POR LA CONSOLA.

n = int(input('INTRODUCE UN NÚMERO ENTERO ENTRE EL 11 Y EL 20: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')

for i in range(11, 21):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')

f.close()