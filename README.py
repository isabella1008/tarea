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
        accion = int(input("---------- \n1.Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n---------- \nAccion: ").strip())
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
    if accion == 2:
        pass
    if accion == 3:
        pass
    if accion == 4:
        pass
    if accion == 5:
        pass
    else:
        break
