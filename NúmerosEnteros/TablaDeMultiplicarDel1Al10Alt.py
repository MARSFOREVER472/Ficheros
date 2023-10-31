# ESCRIBIR UNA FUNCIÓN QUE PIDA UN NÚMERO ENTERO ENTRE EL 1 Y EL 10 Y LO GUARDE EN UN FICHERO CON EL NOMBRE tabla-n.txt LA TABLA DE MULTIPLICAR DE ESE NÚMERO, EN DONDE "n" ES EL NÚMERO INTRODUCIDO POR LA CONSOLA.

n = int(input('INTRODUCE UN NÚMERO ENTERO ENTRE 1 Y 10: '))
name_fichero = 'tabla-' + str(n) + '.txt'
with open(name_fichero, 'w') as f:

    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')