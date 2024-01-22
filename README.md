# Ficheros

_Aunque los ficheros se podrían encajar en más de un apartado de «entrada/salida» ya que representan un medio de almacenamiento persistente, también podrían ser vistos como estructuras de datos, puesto que nos permiten guardar la información y asignarles un cierto formato._ 

- Un fichero es un conjunto de datos relacionados entre sí, que son almacenados de forma permanente en dispositivos tales como discos duros, memorias flash, etc. y que pueden ser tratados, hasta cierto punto, como una unidad.

- En este contexto, permanente quiere decir que, salvo fallos catastróficos o hasta que sean borrados a propósito, estos datos permanecen en el medio en que se almacenan (medios magnéticos o de otro tipo) y continúan existiendo después de que el programa que los creó deja de ejecutarse, incluso después de apagar el ordenador.

- Esto marca la diferencia con los datos que son provisionalmente almacenados en la memoria RAM, la memoria volátil del ordenador, que no sobreviven al programa que los crea y mucho menos a la desconexión del computador de la red eléctrica.

## **Lectura de un fichero**

Python ofrece la función open() para «abrir» un fichero. Esta apertura se puede realizar en 3 modos distintos:

- Lectura del contenido de un fichero existente.

- Escritura del contenido en un fichero nuevo.

- Añadido al contenido de un fichero existente.
