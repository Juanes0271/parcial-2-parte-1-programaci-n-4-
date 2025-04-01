from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto):
        """Agrega un producto a la factura"""
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_info(self):
        """Muestra la información de la factura"""
        print(f"\n📅 Fecha: {self.fecha}")
        print("🛒 Productos comprados:")
        for producto in self.productos:
            print(f"   - {producto.nombre} | ${producto.precio:.2f}")
        print(f"💰 Total: ${self.total:.2f}")
