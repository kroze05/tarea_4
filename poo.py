class Persona():
    def __init__(self,email,direccion,telefono):
        self.email=email
        self.direccion=direccion
        self.telefono = telefono

class Fisica(Persona):
    def __init__(self,email,direccion,telefono,DNI):
        super().__init__(email,direccion,telefono)
        self.DNI=DNI
    def __str__(self):
        return f"email: {self.email}, direccion: {self.direccion}, telefono: {self.telefono}, DNI: {self.DNI}"

class Juridica(Persona):
    def __init__(self,email,direccion,telefono,ci):
        super().__init__(email,direccion,telefono)
        self.ci=ci
    def __str__(self):
        return f"email: {self.email}, direccion: {self.direccion}, telefono: {self.telefono}, CI: {self.ci}"

class Animal ():
    def __init__(self,tipo,nombre,edad):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"raza: {self.tipo}, nombre: {self.nombre}, edad: {self.edad}"

class Historico(Animal):
    def __init__(self,ref_historico):
        self.ref_historico = ref_historico
    def __str__(self):
        return f"referencia historica {self.ref_historico}"

class ElementoHistorico(Historico):
    pass

class Diagnostico():
    def __init__(self,fecha,descripcion):
        self.fecha = fecha
        self.descripcion=descripcion
    def __str__(self):
        return f"fecha:{self.fecha} descripcion: {self.descripcion}"

class Personal ():
    def __init__(self,nombre,apellidos,fecha_cont):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_cont = fecha_cont
    def __str__(self):
        return f"nombre de personal:{self.nombre} apellidos: {self.apellidos} fecha de contratacion: {self.fecha_cont}"

class Veterinario(Personal):
    pass

class Auxiliar(Personal):
    pass

class Factura():
    def __init__(self,ref_factura):
        self.ref_factura= ref_factura
    def __str__(self):
        return f"la referencia de factura {self.ref_factura}"

class ElementoFactura():
    def __init__(self,elemento,precio,cantidad):
        self.elemento=elemento
        self.precio=precio
        self.cantidad=cantidad
    def __str__(self):
        return f"el elemento {self.elemento} con precio {self.precio} la cantidad a adquirir {self.cantidad}"

persona_juridica = Juridica("jeremias@hotmail.com","Sangolqui","0987206013","1727422634")
print(persona_juridica)
perro1 = Animal("golden","huesos","2")
print(perro1)