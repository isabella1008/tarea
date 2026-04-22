# tarea
Concierto_1 = []
Concierto_2 = []
dias_1 = []
dias_2 = []
dias_3 = []
tipos_plan = []

print("SISTEMA DE PLANIFICACIÓN DE VENTA DE ENTRADAS A CONCIERTOS")

while True:
    try:
        accion = int(input("---------- \n1.Generar plan de ventas \n2. Ingresar entradas vendidas \n3. Visualizar ingreso total por concierto \n4. Visualizar ingreso total por día \n5. Salir del programa \n---------- \nAccion: ").strip())
    except:
        print("Error, debe ingresar un numero valido")
    if accion == 1:
        break
    
