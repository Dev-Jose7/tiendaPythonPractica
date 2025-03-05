nombreVendedor = None
productos = []
producto = {}

opcion = 100

print("Mercado")
print("*******")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Modificar producto")
print("4. Eliminar producto")
print("Presiona 5 para salir")
while opcion != 5:
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        print("Bienvenido a la creación de tu lista de mercado")

        #Creando claves y valores de un diccionario
        producto["id"] = 5
        producto["nombre"] = input("Digita el nombre del producto")
        producto["precio"] = int(input("Digita el precio del producto"))
        producto["cantidad"] = int(input("¿Cuantos elementos de este producto vas a llevar: ?"))
        producto["presentación"] = input("¿Cual presentación llevaras?")
        
        # Mostrando mi diccionario
        print(producto)

        # Llnar la lista
        productos.append(producto)
        print(productos)
        
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    else:
        print("opción no valida")