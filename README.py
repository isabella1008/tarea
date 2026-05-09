matriz = []
precio = 18500
MAX_ENTRADAS_POR_DIA = 4000 #maximo de entradas que podemos anotar.

def ingresar_entradas(matriz):  #funcion para ingresar la cantidad de entradas.
    if not matriz: #se ocupa para revisar que la matriz se haya creado
        print("\nError: primero debe generar el plan de ventas (Opción 1).\n")
        return matriz
    num_conciertos = len(matriz)
    num_dias = len(matriz[0])
    print("\nIngresar la cantidad de entradas por concierto y día")
    for i in range(num_conciertos):
        print(f"\nConcierto {i + 1}\n")
        for j in range(num_dias):
            while True:
                try:
                    cantidad = int(input(f"Ingrese cantidad de entradas vendidas en el día {j + 1}: "))
                    if cantidad < 0:
                        print("Error: la cantidad no puede ser negativa.")
 
                    elif cantidad > MAX_ENTRADAS_POR_DIA:
                        print(f"Error, la cantidad de entradas máximo a vender por día es {MAX_ENTRADAS_POR_DIA}.")
                    else:
                        matriz[i][j] = cantidad
                        break  # si cumple con las condiciones sale del while.
                except ValueError:
                    print("  Error: ingrese un número entero válido.")
    mostrar_matriz(matriz) #genera la vista de la matriz con los datos actualizados.
    return matriz
def mostrar_matriz(matriz): #con esta funcion se muestra la matriz en la terminal
    num_dias = len(matriz[0])
    print("\nPlan de ventas")
    print("*" * 45)
    encabezado = " " * 15  #se coloca el titulo de los dias ingresados en tabla
    for j in range(num_dias):
        encabezado += f"{j + 1:>4}"
    print(encabezado)
    for i in range(len(matriz)):     #estas son las filas del concierto
        fila = f"Concierto {i + 1:<5}"
        for valor in matriz[i]:
            fila += f"{valor:>5}"
        print(fila)
    print("*" * 45)
print("\nMENÚ")
while True:
    try:
        accion = int(input("\nSISTEMA DE PLANIFICACIÓN DE VENTA DE ENTRADAS A CONCIERTOS\n-------------------------------------------- \n1. Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n-------------------------------------------- \n\nSeleccione su opción: ").strip())
    except:
        print("Error, debe ingresar un numero valido")
        continue
    if accion == 1:
        print("\nGenerar plan de reserva\n")
        matriz = []
        conciertos = int(input("Ingrese el numero de conciertos: "))  # filas
        dias = int(input("Ingrese numero de días de ventas: "))   # columnas
        for i in range(conciertos):  # i = concierto (fila)
            fila = []
            for j in range(dias):  # j = día (columna)
                fila.append(0)  # parte en 0 porque no hay ventas
            matriz.append(fila)
        # mostrar tabla
        print("\nPlan de ventas")
        print("*" * 40)
        # días arriba
        print(" " * 15, end="")
        for d in range(dias):
            print(f"{d+1:>5}", end="")
        print()
        # mostrar conciertos y datos
        for i in range(conciertos):  # recorro cada fila
            print(f"Concierto {i+1:<5}", end="")
            for j in range(dias):  # recorro cada columna
                print(f"{matriz[i][j]:>5}", end="")  # valor en fila i, columna j
            print()
        print("*" * 40)
    elif accion == 2:
        matriz = ingresar_entradas(matriz)
    elif accion == 3:
        if not matriz:
            print("Error: primero debe generar el plan de ventas")
            continue
        while True:
            print("\nVisualizar el ingreso total de un concierto especifico")
            try:
                concierto = int(input("\nIngrese el concierto a calcular y visualizar: \n").strip())
                if concierto < 1 or concierto > len(matriz):
                    print("ERROR, concierto fuera de rango")
                    continue
                break
            except:
                print("Error, debe ingresar un numero valido")
                continue
        total_concierto = 0
        texto = ""  # acumulador para archivo
        for j in range(len(matriz[concierto-1])):
            entradas = matriz[concierto-1][j]
            ingreso = entradas * precio
            linea = f"Concierto {concierto}, Día {j+1}: ${ingreso:,}"
            print(linea)
            texto += linea + "\n"
            total_concierto = total_concierto + ingreso
        total_linea = f"Total de ingresos del Concierto {concierto}: ${total_concierto:,}"
        print(total_linea)
        texto += total_linea
        with open("concierto.txt", "w", encoding="utf-8") as f:  # escribir archivo
            f.write(texto)

    elif accion == 4:
        if not matriz:
            print("ERROR: Primero debe generar el plan de ventas")
            continue
        while True:
            print("\nVisualizar el ingreso total de un todas los concierto en un dia especifico\n")
            try:
                dia = int(input("Ingrese el día a calcular y visualizar: ").strip())
                if dia < 1 or dia > len(matriz[0]):
                    print("ERROR, día fuera de rango")
                    continue          
            except:
                print("Error, debe ingresar un numero valido")
                continue
            total_dia = 0
            texto = ""
            for i in range(len(matriz)):
                entradas = matriz[i][dia-1]
                ingreso = entradas * precio

                linea = f"Concierto {i+1}, Día {dia}: ${ingreso:,}"
                print(linea)
                texto += linea + "\n"
                total_dia += ingreso
    
            total_linea = f"Total de ingresos del día {dia}: ${total_dia:,}"
            print(total_linea)
            texto += total_linea
            with open("dia.txt", "w") as f:
                f.write(texto)
            break
    elif accion == 5: #termino del programa
        input("Fin de la ejecución del programa")
        break #termina el while
    else:
        print("ERROR, porfavor seleccione una de las opciones disponibles (1, 2, 3, 4 o 5)") #error si el usuario no ingresa ninguna opcion
