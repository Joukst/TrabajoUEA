# Clase base Empleado
class Empleado:
    def __init__(self, nombre, id_empleado, salario):
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__salario = salario

    # Métodos para acceder a los atributos privados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_id_empleado(self):
        return self.__id_empleado

    def obtener_salario(self):
        return self.__salario

    # Método para mostrar información del empleado
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"ID Empleado: {self.__id_empleado}")
        print(f"Salario: ${self.__salario}")

    # Método para calcular el bono del empleado (puede ser sobrescrito por clases derivadas)
    def calcular_bono(self):
        return self.__salario * 0.10


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario, departamento):
        super().__init__(nombre, id_empleado, salario)
        self.departamento = departamento

    # Sobrescribir el método mostrar_informacion para incluir información adicional
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    # Sobrescribir el método calcular_bono para gerentes
    def calcular_bono(self):
        return self.obtener_salario() * 0.20


# Crear instancias de las clases y demostrar funcionalidad
if __name__ == "__main__":
    # Instancia de la clase base Empleado
    empleado1 = Empleado("Juan Pérez", 1001, 50000)
    empleado1.mostrar_informacion()
    print(f"Bono: ${empleado1.calcular_bono()}")

    print("\n")  # Separador

    # Instancia de la clase derivada Gerente
    gerente1 = Gerente("Ana Gómez", 1002, 80000, "Ventas")
    gerente1.mostrar_informacion()
    print(f"Bono: ${gerente1.calcular_bono()}")