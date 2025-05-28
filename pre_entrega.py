 Declaracion de variables (Globales)

# Declaramos la lista de productos, que va a almacenar los siguientes datos
# nombre, categoria, precio
# La inicializamos con algunos datos para poder testear la opcion 2 - Mostrar productos

lista_productos = [
    ["aereo", "turismo", 1800], 
    ["hotel", "alojamiento", 2500],
    ["excursiones","turismo", 800]
]
while True:
    print("""
          
Menú de opciones:
    1. Alta de producto
    2. Mostrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
""")
    opcion = input("Ingrese su opción: ") # Usuario ingresa su opción


    # Procesamiento
    match opcion :
        case "1":
            # Aqui desarrollar código para el alta de productos
            # Ingreso de datos del producto
            # nombre, categoría, y precio
            # Nota: valiamos nombre, categoria y precio
           print("Procesando alta de productos...")
           while True:
                exit_input = input("Ingrese Fin para salir o ENTER para continuar: ").strip().capitalize()
                if exit_input == "Fin":
                    break

                # Validación para el nombre del producto
                while True:
                    nombre = input("Ingrese nombre del producto: ").strip().capitalize()
                    if nombre:
                        break # Sale del bucle si el nombre no está vacío
                    else:
                        print("El nombre del producto no puede estar vacío. Intente de nuevo.")

                # Validación para la categoría del producto
                while True:
                    categoria = input("Ingrese categoría del producto: ").strip().capitalize()
                    if categoria:
                        break # Sale del bucle si la categoría no está vacía
                    else:
                        print("La categoría no puede estar vacía. Intente de nuevo.")

                # Validación para el precio del producto
                while True:
                    precio_input = input("Ingrese el precio del producto: ").strip()
                    if not precio_input:
                        print("El precio no puede estar vacío. Intente de nuevo.")
                    elif not precio_input.isdigit():
                        print("El precio debe ser un número entero. Intente de nuevo.")
                    else:
                        precio = int(precio_input)
                        if precio <= 0:
                            print("El precio debe ser un número positivo. Intente de nuevo.")
                        else:
                            break # Sale del bucle si el precio es un número entero positivo
                
                productos = [nombre, categoria, precio]
                lista_productos.append(productos)
                print(f"Producto '{nombre}' agregado exitosamente.")

    
        case "2":
            print("Procesando mostrar productos...")
            if not lista_productos: # Verifica si la lista está vacía
                print("No hay productos registrados para mostrar.")
            else:
                print("\n" + "-"*50) # Ajustado el ancho para mejor visualización
                print("         Visualización de productos registrados")
                print("-"*50)
                print(f"Número\t Nombre\t\t Categoría\t Precio") # Agregado tabulaciones para alinear
                print("-"*50)
                for id, producto in enumerate(lista_productos): # Usa enumerate para obtener el índice y el producto
                    # Ajusta la alineación para que se vea mejor
                    print(f" {id}\t {producto[0]:<15}\t {producto[1]:<10}\t {producto[2]}") 
                print("-" * 50) # Línea de cierre
                
        case "3":
            print("Procesando búsqueda de productos...")
            if not lista_productos:
                print("No hay productos para buscar.")
                continue

            producto_a_buscar = input("Ingrese el nombre, categoría o precio (número) del producto que desea buscar: ").strip().lower()
            
            encontrados = [] #Declarando lista vacía
            for producto in lista_productos:
               # nombre, categoria, precio = producto[0], producto[1], producto[2]

                # Busca en nombre, categoría o si el precio coincide (convirtiendo a str para la búsqueda)
                if producto_a_buscar in producto[0].strip().lower() or producto_a_buscar in producto[1].strip().lower():
                     encontrados.append(producto)
            
            if not encontrados: # Si la lista de encontrados está vacía
                print(f"No se encontraron resultados para '{producto_a_buscar}'.")
            else:
                print("\n" + "-"*50)
                print("         Resultados de la búsqueda")
                print("-"*50)
                print(f"Número\t Nombre\t\t Categoría\t Precio")
                print("-"*50)
                for id, producto in enumerate(encontrados):
                    print(f" {id}\t {producto[0]:<15}\t {producto[1]:<10}\t {producto[2]}")
                print("-" * 50)

        case "4":
            print("Procesando eliminación de productos...")
            if not lista_productos:
                print("No hay productos para eliminar.")
                continue

            # Primero mostramos los productos para que el usuario sepa qué eliminar
            print("\nProductos actuales:")
            for id, producto in enumerate(lista_productos):
                print(f" {id}. {producto[0]} ({producto[1]}) - ${producto[2]}")
            
            try:
                indice_eliminar_str = input("Ingrese el número del producto a eliminar: ").strip()
                if not indice_eliminar_str.isdigit():
                    print("Por favor, ingrese un número válido.")
                    continue 
                
                indice_eliminar = int(indice_eliminar_str)
                 
                if 0 <= indice_eliminar < len(lista_productos): # Validamos el índice
                    producto_eliminado = lista_productos.pop(indice_eliminar)
                    print(f"Producto '{producto_eliminado[0]}' eliminado exitosamente.")
                else:
                    print("Número de producto inválido. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
            
        case "5":
            print("Saliendo...")
            break # Sale del bucle while True

        case _: # Opción por defecto para cualquier otra entrada
            print("Opción incorrecta. Por favor, elija una opción válida (1-5).")

print("Gracias por usar mi App. ¡Hasta pronto!")
