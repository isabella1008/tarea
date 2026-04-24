# tarea
Concierto_1 = []
Concierto_2 = []
dias_1 = []
dias_2 = []
dias_3 = []
tipos_plan = []
plan_ventas = []

print("SISTEMA DE PLANIFICACIÓN DE VENTA DE ENTRADAS A CONCIERTOS")

while True:
    try:
        accion = int(input("---------- \n1. Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n---------- \nAccion: ").strip())
    except:
        print("Error, debe ingresar un numero valido")
    if accion == 1:
        conciertos = int(input("Ingrese número de conciertos: "))  # filas
        dias = int(input("Ingrese número de días de ventas: "))    # columnas

        for i in range(conciertos):  # i = concierto (fila)
            fila = []
            for j in range(dias):  # j = día (columna)
                fila.append(0)  # parte en 0 porque no hay ventas
            plan_ventas.append(fila)

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
                print(f"{plan_ventas[i][j]:>5}", end="")  # valor en fila i, columna j
            print()

        print("*" * 40)
    elif accion == 2:
        pass
    elif accion == 3:
        pass
    elif accion == 4:
        try:
            dia_calcular = int(input("ingrese el dia a visualizar y calcular: ").strip())
        except:
            print("Error, debe ingresar un numero valido")
        if dia_calcular == 1:
            print("concierto 1, dia 1: ", monto_total11) #muestra el total del concierto 1, dia 1
            print("concierto 2, dia 1: ", monto_total12) #muestra el total del concierto 2, dia 1
            total_dia1 = monto_total11 + monto_total12 #se suman las ganancias totales del dia 1
            print("ingreso total dia 1: ", total_dia1) #se le muestra al usuario las ganancias totales del dia 1
        elif dia_calcular == 2: 
            print("concierto 1, dia 2: ", monto_total21) #muestra el total del concierto 1, dia 2
            print("concierto 2, dia 2: ", monto_total22) #muestra el total del concierto 2, dia 2
            total_dia2 = monto_total21 + monto_total22 #se suman las ganancias totales del dia 2
            print("ingreso total dia 2: ", total_dia2) #se le muestra al usuario las ganancias totales del dia 2
        elif dia_calcular == 3:
            print("concierto 1, dia 3: ", monto_total31) #muestra el total del concierto 1, dia 3
            print("concierto 2, dia 3: ", monto_total32) #muestra el total del concierto 2, dia 3
            total_dia3 = monto_total31 + monto_total32 #se suman las ganancias totales del dia 3
            print("ingreso total dia 3: ", total_dia3) #se le muestra al usuario las ganancias totales del dia 3
        else:
            print("ERROR, porfavor seleccione solo 1 de los dias disponibles (1, 2, 3)") #error si el usuario ingresa calquier cosa 
    elif accion == 5: #termino del programa
        print("hasta luego👋")
        input("presione enter para cerrar...")
        break #termina el while
    else:
        print("ERROR, porfavor seleccione una de las opciones disponibles (1, 2, 3, 4 o 5)") #error si el usuario no ingresa ninguna opcion
    
