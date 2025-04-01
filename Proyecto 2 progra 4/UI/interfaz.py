from Modelos.clientes import Cliente
from Modelos.facturas import Factura
from Modelos.productos import Antibiotico, ControlPlagas, ControlFertilizantes

clientes = []  # Lista de clientes registrados

def crear_cliente():
    """Solicita los datos del cliente y lo agrega a la lista"""
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    print("✅ Cliente registrado con éxito.")

def seleccionar_cliente():
    """Permite seleccionar un cliente por cédula"""
    cedula = input("Ingrese la cédula del cliente: ")
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    print("❌ Cliente no encontrado.")
    return None

def crear_factura():
    """Crea una factura para un cliente existente"""
    cliente = seleccionar_cliente()
    if cliente:
        factura = Factura(cliente)
        cliente.agregar_factura(factura)
        print("✅ Factura creada con éxito.")

        while True:
            print("\n📌 Agregar Producto a la Factura:")
            print("1. Antibiótico")
            print("2. Control de Plagas")
            print("3. Control de Fertilizantes")
            print("4. Finalizar Factura")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre del antibiótico: ")
                precio = float(input("Precio: "))
                dosis = int(input("Dosis (400Kg - 600Kg): "))
                tipo_animal = input("Tipo de animal (Bovino, Caprino, Porcino): ")
                producto = Antibiotico(nombre, precio, dosis, tipo_animal)

            elif opcion == "2":
                nombre = input("Nombre del control de plagas: ")
                precio = float(input("Precio: "))
                registro_ica = input("Registro ICA: ")
                frecuencia = input("Frecuencia de aplicación (días): ")
                periodo_carencia = input("Periodo de carencia (días): ")
                producto = ControlPlagas(nombre, precio, registro_ica, frecuencia, periodo_carencia)

            elif opcion == "3":
                nombre = input("Nombre del fertilizante: ")
                precio = float(input("Precio: "))
                registro_ica = input("Registro ICA: ")
                frecuencia = input("Frecuencia de aplicación (días): ")
                fecha_ultima = input("Fecha de última aplicación: ")
                producto = ControlFertilizantes(nombre, precio, registro_ica, frecuencia, fecha_ultima)

            elif opcion == "4":
                break

            else:
                print("⚠️ Opción no válida.")
                continue

            factura.agregar_producto(producto)
            print(f"✅ {producto.nombre} agregado a la factura.")

def mostrar_clientes():
    """Muestra todos los clientes y sus facturas"""
    if not clientes:
        print("📭 No hay clientes registrados.")
        return
    for cliente in clientes:
        cliente.mostrar_info()

def menu():
    """Muestra el menú principal"""
    while True:
        print("\n🌟 Menú Principal 🌟")
        print("1. Registrar Cliente")
        print("2. Crear Factura")
        print("3. Mostrar Clientes y Facturas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            crear_factura()
        elif opcion == "3":
            mostrar_clientes()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Gracias por usar nuestro sistema de facturación!")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")
