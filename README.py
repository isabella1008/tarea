# SISTEMA DE SOLICITUD DE PRODUCTOS TECNOLÓGICOS
# Opción 1 completa
try:
    import csv
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    pass
ARCHIVO_CLIENTES = "clientes.csv"
###ARCHIVO_RESERVAS = "reservas.csv"###
# CLASE CLIENTE
class Cliente:
    def __init__(self, rut, nombres, apellido_p, apellido_m, telefono, email, direccion, presupuesto):
        self.rut = rut
        self.nombres = nombres
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.presupuesto = int(presupuesto)
    def convertir_lista(self):
        return [self.rut, self.nombres, self.apellido_p, self.apellido_m, self.telefono, self.email, self.direccion, self.presupuesto]
    def mostra(self):

        print("-----------------------------")
        print("Rut:", self.rut)
        print("Nombres:", self.nombres)
        print("Apellido paterno:", self.apellido_p)
        print("Apellido materno:", self.apellido_m)
        print("Teléfono:", self.telefono)
        print("Email:", self.email)
        print("Dirección:", self.direccion)
        print("Presupuesto:", self.presupuesto)
        print("-----------------------------")
# FUNCIONES AUXILIARES
def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Debe ser un número positivo.")
            else:
                return numero
        except ValueError:
            print("Debe ingresar un número.")
def guardar_clientes(clientes):
    with open(ARCHIVO_CLIENTES, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for cliente in clientes:
            escritor.writerow(cliente.convertir_lista())
def cargar_clientes():
    clientes = []
    try:
        with open(ARCHIVO_CLIENTES, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                cliente = Cliente(
                    fila[0],fila[1],fila[2],fila[3],
                    fila[4],fila[5],fila[6], fila[7])
                clientes.append(cliente)
    except FileNotFoundError:
        pass
    return clientes
# OPCIÓN 1
def ingresar_cliente(clientes):
    print("\nIngrese los siguientes datos:\n")
    rut = input("Rut: ")
    for cliente in clientes:
        if cliente.rut == rut:
            print("Ese cliente ya existe.")
            return
    nombres = input("Nombres: ")
    apellido_p = input("Apellido paterno: ")
    apellido_m = input("Apellido materno: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    direccion = input("Dirección: ")
    presupuesto = leer_entero("Presupuesto disponible: ")
    nuevo = Cliente(rut, nombres, apellido_p, apellido_m, telefono, email, direccion, presupuesto)
    clientes.append(nuevo)
    guardar_clientes(clientes)
    print("\nCliente registrado correctamente.\n")
# OPCIÓN 3 (solo para probar)
def visualizar_clientes(clientes):
    if len(clientes) == 0:
        print("\nNo existen clientes registrados.\n")
        return
    print("\nCLIENTES REGISTRADOS\n")
    for cliente in clientes:
        cliente.mostrar()

# GESTIÓN DE PRODUCTOS SOLICITADOS
ARCHIVO_PRODUCTOS = "productos.csv"

# CLASE PRODUCTO
class Producto:
    def __init__(self, rut_cliente, nombre_producto, categoria, cantidad, precio_unitario):
        self.rut_cliente = rut_cliente
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.cantidad = int(cantidad)
        self.precio_unitario = int(precio_unitario)

    def total(self):
        return self.cantidad * self.precio_unitario

    def convertir_lista(self):
        return [self.rut_cliente, self.nombre_producto, self.categoria,
                self.cantidad, self.precio_unitario]

    def mostrar(self):
        print("-----------------------------")
        print("RUT cliente:", self.rut_cliente)
        print("Producto:", self.nombre_producto)
        print("Categoría:", self.categoria)
        print("Cantidad:", self.cantidad)
        print("Precio unitario:", self.precio_unitario)
        print("Total:", self.total())
        print("-----------------------------")

# FUNCIONES DE ARCHIVO (PRODUCTOS)
def guardar_productos(productos):
    with open(ARCHIVO_PRODUCTOS, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for producto in productos:
            escritor.writerow(producto.convertir_lista())

def cargar_productos():
    productos = []
    try:
        with open(ARCHIVO_PRODUCTOS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                producto = Producto(fila[0], fila[1], fila[2], fila[3], fila[4])
                productos.append(producto)
    except FileNotFoundError:
        pass
    return productos

# OPCIÓN 2: Ingresar producto solicitado
def ingresar_producto(clientes, productos):
    if len(clientes) == 0:
        print("\nNo hay clientes registrados. Debe ingresar un cliente primero.\n")
        return

    rut = input("\nIngrese el RUT del cliente que solicita el producto: ")

    cliente_encontrado = None
    for cliente in clientes:
        if cliente.rut == rut:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("\nNo existe un cliente con ese RUT. Debe registrarlo primero.\n")
        return

    print(f"\nCliente encontrado: {cliente_encontrado.nombres} {cliente_encontrado.apellido_p}")

    nombre_producto = input("Nombre del producto: ")
    categoria = input("Categoría (notebook, celular, accesorio, etc.): ")
    cantidad = leer_entero("Cantidad: ")
    precio_unitario = leer_entero("Precio unitario: ")

    nuevo_producto = Producto(rut, nombre_producto, categoria, cantidad, precio_unitario)

    if nuevo_producto.total() > cliente_encontrado.presupuesto:
        print("\nAviso: el total del producto supera el presupuesto del cliente.\n")

    productos.append(nuevo_producto)
    guardar_productos(productos)
    print("\nProducto registrado correctamente.\n")

# OPCIÓN 4: Visualizar productos solicitados
def visualizar_productos(productos, clientes):
    if len(productos) == 0:
        print("\nNo existen productos solicitados registrados.\n")
        return

    print("\nPRODUCTOS SOLICITADOS\n")
    for producto in productos:
        nombre_cliente = "Desconocido"
        for cliente in clientes:
            if cliente.rut == producto.rut_cliente:
                nombre_cliente = f"{cliente.nombres} {cliente.apellido_p}"
                break
        print(f"Cliente: {nombre_cliente}")
        producto.mostrar()

# ============================================================
# MENÚ
# ============================================================
def mostrar_menu():
    print()
    print("============================================")
    print("SISTEMA DE SOLICITUD DE PRODUCTOS TECNOLÓGICOS")
    print("============================================")
    print("1. Ingresar datos de clientes")
    print("2. Ingresar productos solicitados")
    print("3. Visualizar datos de clientes")
    print("4. Visualizar productos solicitados")
    print("5. Visualizar gráfico del presupuesto")
    print("6. Salir")
# MAIN
def main():
    clientes = cargar_clientes()
    productos = cargar_productos()
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue
        if opcion == 1:
            ingresar_cliente(clientes)
        elif opcion == 2:
            ingresar_producto(clientes, productos)
        elif opcion == 3:
            visualizar_clientes(clientes)
        elif opcion == 4:
            visualizar_productos(productos, clientes)
        elif opcion == 5:
            print("\nOpción en construcción.\n")
        elif opcion == 6:
            print("\nPrograma finalizado.")
            break
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    main()

🔹 Persona 3: Validaciones del sistema (lógica del problema)

Responsabilidad principal: reglas del negocio.

Validar stock disponible
Validar presupuesto del cliente
Reintentos cuando datos no cumplen condiciones (como en el ejemplo)
Calcular costo total (precio × cantidad)

👉 Muy importante: aquí se gana mucho puntaje en la rúbrica (lógica + integración).

🔹 Persona 4: Manejo de archivos (lectura/escritura)

Responsabilidad principal: persistencia de datos.

Guardar clientes en archivo
Guardar productos en archivo
Leer datos desde archivo al iniciar el programa
Usar modos: lectura, escritura y/o append

👉 Este módulo es crítico porque vale hartos puntos en la rúbrica.

🔹 Persona 5: Menú principal + gráfico

Responsabilidad principal: interacción y flujo del programa.

Crear el menú principal con todas las opciones
Controlar el loop del programa (while)
Llamar a las funciones de los demás
Implementar opción 5: gráfico del presupuesto
Puede usar matplotlib (recomendado)
Opción 6: salida del programa

👉 Este rol integra todo el sistema.
