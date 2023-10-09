
class Cliente: 

    carrito_de_compras = []

    def __init__(self, nombre, apellido, dni, edad, domicilio):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.domicilio = domicilio

    def __str__(self):
        print(f'El cliente {self.nombre} {self.apellido},  con DNI: {self.dni}, tiene {self.edad} años y su domicilio es {self.domicilio}')

    def modificar_domicilio(self, domicilio_nuevo):
        self.domicilio = domicilio_nuevo
        print(f"El domicilio de modifico con exito, el domicilio actual es: {self.domicilio}")

    def agregar_producto(self, producto):
        self.carrito_de_compras.append(producto)

    def mostrar_carrito(self):
        print(self.carrito_de_compras)            

cliente1= Cliente("Rodrigo", "Lezama", "36404947", "32", "calle falsa 123") 

cliente1.agregar_producto("pera")
cliente1.mostrar_carrito()
cliente1.__str__()
cliente1.modificar_domicilio("calle falsa 234")