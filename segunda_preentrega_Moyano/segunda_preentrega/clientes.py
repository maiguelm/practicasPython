class Cliente:
    def __init__(self, razon_social, correo, domicilio, telefono):
        self.razon_social = razon_social
        self.correo = correo
        self.domicilio = domicilio
        self.telefono = telefono

    def __str__(self):
        return ' Razon Social: {} \n E-mail: {} \n Domicilio: {} \n Telefono: {}'.format(self.razon_social, self.correo, self.domicilio, self.telefono)
    
    def compra(self, precio):
        return f'El cliente {self.razon_social} ha realizado una compra por $ {precio}'
    
class ClienteMinorista(Cliente):
    def __init__(self, razon_social, correo, domicilio, telefono, dni, tarjeta, cuotas):
        super().__init__(razon_social, correo, domicilio, telefono)
        self.dni = dni
        self.tarjeta = tarjeta
        self.cuotas = cuotas
    
    def __str__(self):
        return super().__str__() + '\n DNI: {} \n Tarjetas: {} \n Cuotas: {}'.format(self.dni, self.tarjeta, self.cuotas)
        
class ClienteMayorista(Cliente):
    def __init__(self, razon_social, correo, domicilio, telefono, cuit, iva, cuenta_corriente):
        super().__init__(razon_social, correo, domicilio, telefono)
        self.cuit = cuit
        self.iva = iva
        self.cuenta_corriente = cuenta_corriente
    
    def __str__(self):
        return super().__str__() + '\n CUIT: {} \n Condicion frente al IVA: {} \n Tiene cuenta corriente: {}'.format(self.cuit, self.iva, self.cuenta_corriente)
        
