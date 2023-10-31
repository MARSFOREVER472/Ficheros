# Ficheros

Aunque los ficheros encajarían más en un apartado de «entrada/salida» ya que representan un medio de almacenamiento persistente, también podrían ser vistos como estructuras de datos, puesto que nos permiten guardar la información y asignarles un cierto formato. 1

Un fichero es un conjunto de bytes almacenados en algún dispositivo. El sistema de ficheros es la estructura lógica que alberga los ficheros y está jerarquizado a través de directorios (o carpetas). Cada fichero se identifica unívocamente a través de una ruta que nos permite acceder a él.

Lectura de un fichero
Python ofrece la función open() para «abrir» un fichero. Esta apertura se puede realizar en 3 modos distintos:

- Lectura del contenido de un fichero existente.

- Escritura del contenido en un fichero nuevo.

- Añadido al contenido de un fichero existente.
