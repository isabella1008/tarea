# SISTEMA DE SOLICITUD DE PRODUCTOS TECNOLÓGICOS
try:
    import csv
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    pass

ARCHIVO_CLIENTES = "clientes.csv"

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
        return [self.rut, self.nombres, self.apellido_p, self.apellido_m,
                self.telefono, self.email, self.direccion, self.presupuesto]

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

# =========================
# PERSONA 4 (TU PARTE)
# =========================

def guardar_cliente_individual(cliente):
    with open(ARCHIVO_CLIENTES, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(cliente.convertir_lista())

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
                cliente = Cliente(fila[0],fila[1],fila[2],fila[3],
                                  fila[4],fila[5],fila[6], fila[7])
                clientes.append(cliente)
    except FileNotFoundError:
        pass
    return clientes

# OPCIÓN 1
def ingresar_cliente(clientes):
    print("\nIngrese los siguientes datos:\n")

    while True:
        rut = input("Rut: ")
        if rut.strip() == "":
            print("El rut no puede estar vacío.")
        else:
            break

    for cliente in clientes:
        if cliente.rut == rut:
            print("Ese cliente ya existe.")
            return

    while True:
        nombres = input("Nombres: ")
        if nombres.strip() == "" or nombres.isdigit():
            print("Ingrese un nombre válido.")
        else:
            break

    while True:
        apellido_p = input("Apellido paterno: ")
        if apellido_p.strip() == "" or apellido_p.isdigit():
            print("Ingrese un apellido válido.")
        else:
            break

    while True:
        apellido_m = input("Apellido materno: ")
        if apellido_m.strip() == "" or apellido_m.isdigit():
            print("Ingrese un apellido válido.")
        else:
            break

    while True:
        telefono = input("Teléfono: ")
        if telefono.strip() == "" or not telefono.isdigit():
            print("Ingrese un teléfono válido.")
        else:
            break

    while True:
        email = input("Email: ")
        if "@" not in email or "." not in email:
            print("Ingrese un email válido.")
        else:
            break

    while True:
        direccion = input("Dirección: ")
        if direccion.strip() == "":
            print("La dirección no puede estar vacía.")
        else:
            break

    presupuesto = leer_entero("Presupuesto disponible: ")

    nuevo = Cliente(rut, nombres, apellido_p, apellido_m,
                    telefono, email, direccion, presupuesto)

    clientes.append(nuevo)

    guardar_cliente_individual(nuevo)  

    print("\nCliente registrado correctamente.\n")

# OPCIÓN 3
def visualizar_clientes(clientes):
    if len(clientes) == 0:
        print("\nNo existen clientes registrados.\n")
        return
    print("\nCLIENTES REGISTRADOS\n")
    for cliente in clientes:
        cliente.mostra()

# PRODUCTOS
ARCHIVO_PRODUCTOS = "productos.csv"

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

# =========================
# PERSONA 4 (TU PARTE)
# =========================

def guardar_producto_individual(producto):
    with open(ARCHIVO_PRODUCTOS, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(producto.convertir_lista())

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

# OPCIÓN 2 (PERSONA 3)
def ingresar_producto(clientes, productos):
    if len(clientes) == 0:
        print("\nNo hay clientes registrados.\n")
        return

    while True:
        rut = input("\nIngrese el RUT del cliente: ")
        if rut.strip() == "":
            print("El RUT no puede estar vacío.")
        else:
            break

    cliente_encontrado = None
    for cliente in clientes:
        if cliente.rut == rut:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("\nCliente no existe.\n")
        return

    while True:
        nombre_producto = input("Nombre producto: ")
        if nombre_producto.strip() == "":
            print("No puede estar vacío.")
        else:
            break

    while True:
        categoria = input("Categoría: ")
        if categoria.strip() == "" or categoria.isdigit():
            print("Categoría inválida.")
        else:
            break

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Debe ser mayor a 0.")
            else:
                break
        except:
            print("Número inválido.")

    while True:
        try:
            precio = int(input("Precio: "))
            if precio <= 0:
                print("Debe ser mayor a 0.")
            else:
                break
        except:
            print("Número inválido.")

    total = cantidad * precio
    intentos = 0

    while total > cliente_encontrado.presupuesto:
        print("Supera presupuesto.")
        try:
            nuevo = int(input("Nuevo presupuesto: "))
            cliente_encontrado.presupuesto = nuevo
        except:
            print("Error.")

        intentos += 1
        if intentos == 3:
            print("Cancelado.")
            return

    nuevo_producto = Producto(rut, nombre_producto, categoria, cantidad, precio)
    productos.append(nuevo_producto)

    guardar_producto_individual(nuevo_producto)  

    print("\nProducto registrado.\n")

# OPCIÓN 4
def visualizar_productos(productos, clientes):
    if len(productos) == 0:
        print("\nNo existen productos.\n")
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

# MENÚ
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

🔹 Persona 5: Menú principal + gráfico

Responsabilidad principal: interacción y flujo del programa.

Crear el menú principal con todas las opciones
Controlar el loop del programa (while)
Llamar a las funciones de los demás
Implementar opción 5: gráfico del presupuesto
Puede usar matplotlib (recomendado)
Opción 6: salida del programa

👉 Este rol integra todo el sistema.
