matriz = []
precio = 18500
print("SISTEMA DE PLANIFICACIÓN DE VENTA DE ENTRADAS A CONCIERTOS")

while True:
    try:
        accion = int(input("-------------------------------------------- \n1. Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n-------------------------------------------- \nAccion: ").strip())
    except:
        print("Error, debe ingresar un numero valido")
        continue
    if accion == 1:
        matriz = []
        conciertos = 2  # filas
        dias = 3   # columnas
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
        pass
    elif accion == 3:
        pass
    elif accion == 4:
        if not matriz:
            print("ERROR: Primero debe generar el plan de ventas")
            continue
        while True:
            try:
                dia = int(input("Ingrese el día a visualizar (1-3): ").strip())
                if dia < 1 or dia > 3:
                    print("ERROR, seleccione solo 1, 2 o 3")
                    continue
            except:
                print("Error, debe ingresar un numero valido")
            print(f"\nDía {dia}")
            total_dia = 0
            for i in range(len(matriz)):
                entradas = matriz[i][dia-1]
                print(f"Concierto {i+1}: {entradas}")
                total_dia += entradas
            print(f"Total de entradas vendidas y monto: {total_entradas}, monto total {monto_total}")#variables no definidas aun
            break
    elif accion == 5: #termino del programa
        print("hasta luego👋")
        input("presione enter para cerrar...")
        break #termina el while
    else:
        print("ERROR, porfavor seleccione una de las opciones disponibles (1, 2, 3, 4 o 5)") #error si el usuario no ingresa ninguna opcion
