class Archivo:
    # Constructor
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
        self.abrir_archivo()
        print(f'Archivo {self.nombre_archivo} abierto en modo {self.modo}.')

    # Método para abrir el archivo
    def abrir_archivo(self):
        try:
            self.archivo = open(self.nombre_archivo, self.modo)
        except IOError as e:
            print(f'Error al abrir el archivo: {e}')

    # Método para escribir en el archivo
    def escribir(self, contenido):
        if self.archivo and not self.archivo.closed:
            self.archivo.write(contenido + '\n')
        else:
            print('El archivo no está abierto para escritura.')

    # Método para leer el archivo
    def leer(self):
        if self.archivo and not self.archivo.closed:
            return self.archivo.read()
        else:
            print('El archivo no está abierto para lectura.')
            return None

    # Destructor
    def __del__(self):
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f'Archivo {self.nombre_archivo} cerrado.')


# Creación de objetos de la clase Archivo
archivo_escritura = Archivo('example.txt', 'w')
archivo_escritura.escribir('Primera línea de texto.')
archivo_escritura.escribir('Segunda línea de texto.')

# Cambiamos el objeto a modo lectura
archivo_lectura = Archivo('example.txt', 'r')
contenido = archivo_lectura.leer()
print('Contenido del archivo:')
print(contenido)

# Eliminación de objetos para desencadenar el destructor
del archivo_escritura
del archivo_lectura
