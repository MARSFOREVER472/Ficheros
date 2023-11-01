# ESCRIBIR UN PROGRAMA QUE ACCEDA A UN FICHERO DE INTERNET MEDIANTE SU URL Y MUESTRE POR PANTALLA EL NÚMERO DE PALABRAS QUE CONTIENE.

def count_words(url):
    '''
    FUNCIÓN QUE RECIBE LA URL DE UN FICHERO DE TEXTO Y DEVUELVE EL NÚMERO DE PALABRAS QUE CONTIENE.
    PARÁMETROS:
        URL: ES UNA CADENA CON LA URL DEL FICHERO DE TEXTO.
    DEVUELVE:
        EL NÚMERO DE PALABRAS QUE CONTIENE EL FICHERO DE TEXTO DADO POR LA URL.
    '''

    from urllib import request
    from urllib.error import URLError

    try:
        f = request.urlopen(url)
    except URLError:
        return('¡LA URL ' + url + ' NO EXISTE!!!!!')
    else:
        contenido = f.read()
        return len(contenido.split())
    
print(count_words('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(count_words('https://no-existe.txt'))