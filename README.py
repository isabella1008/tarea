🔹 Persona 1: Gestión de clientes

Responsabilidad principal: todo lo relacionado a clientes.

Crear estructura de datos para clientes (listas/diccionarios)
Función para ingresar clientes (opción 1 del menú)
Validar datos básicos (ej: rut no vacío, presupuesto numérico)
Función para mostrar clientes (opción 3)
Preparar datos para guardado en archivo

👉 Parte clave porque define la base del sistema.

🔹 Persona 2: Gestión de productos solicitados

Responsabilidad principal: ingreso y visualización de productos.

Crear estructura de datos para productos
Función para ingresar productos (opción 2)
Relacionar producto con cliente (usar RUT)
Función para mostrar productos (opción 4)

👉 Esta parte es equivalente en complejidad a clientes.

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
