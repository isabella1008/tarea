# tarea
Concierto_1 = []
Concierto_2 = []
dias_1 = []
dias_2 = []
dias_3 = []
tipos_plan = []
matriz = []
 
MAX_ENTRADAS_POR_DIA = 4000 #Para limitar el maximo de entradas.
 
def ingresar_entradas(matriz):  #Se utiliza para ingresar la cantidad de entradas vendidas por concierto.
 
    if not matriz: # Se ocupa para verificar que la matriz ya haya sido creada.
        print("\nError: primero debe generar el plan de ventas (Opción 1).\n")
        return matriz
 
    num_conciertos = len(matriz)
    num_dias = len(matriz[0])
 
    print("\nIngresar la cantidad de entradas por concierto y día")
 
    for i in range(num_conciertos):
        print(f"\nConcierto {i + 1}")
 
        for j in range(num_dias):
            while True:
                try:
                    cantidad = int(input(f"  Ingrese cantidad de entradas vendidas en el día {j + 1}: "))
 
                    if cantidad < 0:
                        print("  Error: la cantidad no puede ser negativa.")
 
                    elif cantidad > MAX_ENTRADAS_POR_DIA:
                        print(f"  Error, la cantidad de entradas máximo a vender por día es {MAX_ENTRADAS_POR_DIA}.")
 
                    else:
                        matriz[i][j] = cantidad
                        break  # Si el valor es válido, sale del while.
 
                except ValueError:
                    print("  Error: ingrese un número entero válido.")
 
    mostrar_matriz(matriz) #Muestra la matriz ya actualizada.
 
    return matriz
 
 
def mostrar_matriz(matriz): #Con esta funcion mostramos la matriz en la terminal con formato tabla
 
    num_dias = len(matriz[0])
 
    print("\nPlan de ventas")
    print("*" * 45)
 
    encabezado = "                  "   # Encabezado de los días en la tabla
    for j in range(num_dias):
        encabezado += f"  {j + 1:>5}"
    print(encabezado)
 
    for i in range(len(matriz)):     # Filas de conciertos
        fila = f"Concierto {i + 1:<4}"
        for valor in matriz[i]:
            fila += f"  {valor:>5}"
        print(fila)
 
    print("*" * 45)
 
 
print("SISTEMA DE PLANIFICACIÓN DE VENTA DE ENTRADAS A CONCIERTOS")
 
while True:
    try:
        accion = int(input("-------------------------------------------- \n1. Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n-------------------------------------------- \nAccion: ").strip())
    except:
        print("Error, debe ingresar un número válido")
        continue
    if accion == 1:
        matriz = []
        conciertos = 2 # filas
        dias = 3 # columnas
 
        for i in range(conciertos): # i = concierto (fila)
            fila = []
            for j in range(dias): # j = día (columna)
                fila.append(0) # parte en 0 porque no hay ventas
            matriz.append(fila)
 
        # se muestra en la tabla
        print("\nPlan de ventas")
        print("*" * 40)
 
        # los están días arriba
        print(" " * 15, end="")
        for d in range(dias):
            print(f"{d+1:>5}", end="")
        print()
 
        # muestra los conciertos y datos
        for i in range(conciertos): # recorre cada fila
            print(f"Concierto {i+1:<5}", end="")
            for j in range(dias): # recorre cada columna
                print(f"{matriz[i][j]:>5}", end="") # valor en fila i, columna j
            print()
 
        print("*" * 40)
    elif accion == 2:
        matriz = ingresar_entradas(matriz)
    elif accion == 3:
        pass
    elif accion == 4:
        try:
            dia_calcular = int(input("ingrese el dia a visualizar y calcular: ").strip())
        except:
            print("Error, debe ingresar un número válido")
            continue
        if dia_calcular == 1:
            print("concierto 1, dia 1: ", monto_total11) #muestra el total del concierto 1, dia 1
            print("concierto 2, dia 1: ", monto_total12) #muestra el total del concierto 2, dia 1
            total_dia1 = monto_total11 + monto_total12 #se suman las ganancias totales del día 1
            print("ingreso total dia 1: ", total_dia1) #se le muestra al usuario las ganancias totales del día 1
        elif dia_calcular == 2:
            print("concierto 1, dia 2: ", monto_total21) #muestra el total del concierto 1, dia 2
            print("concierto 2, dia 2: ", monto_total22) #muestra el total del concierto 2, dia 2
            total_dia2 = monto_total21 + monto_total22 #se suman las ganancias totales del día 2
            print("ingreso total dia 2: ", total_dia2) #se le muestra al usuario las ganancias totales del dia 2
        elif dia_calcular == 3:
            print("concierto 1, dia 3: ", monto_total31) #muestra el total del concierto 1, dia 3
            print("concierto 2, dia 3: ", monto_total32) #muestra el total del concierto 2, dia 3
            total_dia3 = monto_total31 + monto_total32 #se suman las ganancias totales del día 3
            print("ingreso total dia 3: ", total_dia3) #se le muestra al usuario las ganancias totales del dia 3
        else:
            print("ERROR, por favor seleccione solo 1 de los días disponibles (1, 2, 3)") #error si el usuario ingresa calquier cosa
    elif accion == 5: #termino del programa
        print("hasta luego👋")
        input("presione enter para cerrar...")
        break #termina el while
    else:
        print("ERROR, por favor seleccione una de las opciones disponibles (1, 2, 3, 4 o 5)") #error si el usuario no ingresa ninguna opción
