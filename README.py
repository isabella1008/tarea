# SISTEMA DE SOLICITUD DE PRODUCTOS TECNOLÓGICOS
try:
    import csv
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    pass

ARCHIVO_CLIENTES = "clientes.csv"
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

def guardar_cliente_individual(cliente):
    with open(ARCHIVO_CLIENTES, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(cliente.convertir_lista())

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
                                  fila[4],fila[5],fila[6],fila[7])
                clientes.append(cliente)
    except FileNotFoundError:
        pass
    return clientes

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
    nuevo = Cliente(rut, nombres, apellido_p, apellido_m, telefono, email, direccion, presupuesto)
    clientes.append(nuevo)
    guardar_cliente_individual(nuevo)
    print("\nCliente registrado correctamente.\n")
def visualizar_clientes(clientes):
    if len(clientes) == 0:
        print("\nNo existen clientes registrados.\n")
        return
    print("\nCLIENTES REGISTRADOS\n")
    for cliente in clientes:
        cliente.mostra()
ARCHIVO_PRODUCTOS = "productos.csv"

class Producto:
    def __init__(self, rut_cliente, codigo, nombre_producto, categoria, marca, modelo, stock, precio, cantidad):
        self.rut_cliente = rut_cliente
        self.codigo = codigo
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.stock = int(stock)
        self.precio = int(precio)
        self.cantidad = int(cantidad)

    def total(self):
        return self.precio * self.cantidad

    def convertir_lista(self):
        return [self.rut_cliente,self.codigo,self.nombre_producto,self.categoria,self.marca,self.modelo,self.stock,self.precio,self.cantidad]

    def mostrar(self):
        print("Rut:", self.rut_cliente)
        print("Código del producto:", self.codigo)
        print("Nombre del producto:", self.nombre_producto)
        print("Categoría:", self.categoria)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Stock disponible:", self.stock)
        print("Precio:", self.precio)
        print("Cantidad solicitada:", self.cantidad)
        print()
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
                producto = Producto(fila[0],
                    fila[1], fila[2], fila[3], fila[4],
                    fila[5], fila[6], fila[7], fila[8])
                productos.append(producto)
    except FileNotFoundError:
        pass
    return productos

def ingresar_producto(clientes, productos):
    if len(clientes) == 0:
        print("\nNo existen clientes registrados.")
        return
    print("\nIngrese los siguientes datos")
    rut = input("Rut: ")
    cliente = None
    for c in clientes:
        if c.rut == rut:
            cliente = c
            break
    if cliente is None:
        print("Cliente no registrado.")
        return
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    stock = leer_entero("Stock disponible: ")
    precio = leer_entero("Precio: ")
    while True:
        cantidad = leer_entero("Cantidad solicitada: ")
        if cantidad > stock:
            print(f"La cantidad solicitada muy alta, el stock disponible es de: {stock}")
            continue
        total = cantidad * precio
        if total > cliente.presupuesto:
            print(f"Su presupuesto disponible es de {cliente.presupuesto}, el monto de la compra es de {total}")
            continue
        break
    producto = Producto(rut,codigo,nombre,categoria,marca,modelo,stock,precio,cantidad)
    productos.append(producto)
    guardar_producto_individual(producto)
    print("\nProducto registrado correctamente.")

def visualizar_productos(productos):

    if len(productos) == 0:
        print("\nNo existen productos registrados.\n")
        return

    print("\nVisualizar datos de productos solicitados:\n")

    for producto in productos:
        producto.mostrar()
def graficar_presupuestos(clientes):

    if len(clientes) == 0:
        print("\nNo existen clientes registrados.\n")
        return

    nombres = []
    presupuestos = []

    for cliente in clientes:
        nombres.append(cliente.nombres)
        presupuestos.append(cliente.presupuesto)

    plt.figure(figsize=(10,6))

    plt.bar(nombres, presupuestos)

    plt.title("Presupuesto disponible de los clientes")
    plt.xlabel("Clientes")
    plt.ylabel("Presupuesto ($)")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.show()
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
            visualizar_productos(productos)
        elif opcion == 5:
            graficar_presupuestos(clientes)
        elif opcion == 6:
            print("\nPrograma finalizado.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
