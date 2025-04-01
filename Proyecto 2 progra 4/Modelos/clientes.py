class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.historial_compras = []  # Lista de facturas

    def agregar_factura(self, factura):
        """Agrega una factura al historial del cliente"""
        self.historial_compras.append(factura)

    def mostrar_info(self):
        """Muestra la información del cliente y su historial de compras"""
        print(f"\n👤 Cliente: {self.nombre} - Cédula: {self.cedula}")
        if self.historial_compras:
            print("🧾 Historial de Facturas:")
            for factura in self.historial_compras:
                factura.mostrar_info()
        else:
            print("📭 No tiene facturas registradas.")
