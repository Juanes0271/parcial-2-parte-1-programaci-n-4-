class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

class ProductoControl(Producto):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion

class ControlPlagas(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia

class ControlFertilizantes(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

class Antibiotico(Producto):
    def __init__(self, nombre, precio, dosis, tipo_animal):
        super().__init__(nombre, precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal
