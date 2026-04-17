# Nombre
nombre = ""
while not nombre.isalpha():
    nombre = input("Ingrese nombre del cliente: ")
    if not nombre.isalpha():
        print("Error: solo letras")

# Cantidad de productos
cantidad = ""
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Cantidad de productos: ")
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Error: número válido mayor a 0")

cantidad = int(cantidad)

total_sin = 0
total_con = 0

for i in range(1, cantidad + 1):
    precio = ""
    while not precio.isdigit():
        precio = input(f"Producto {i} - Precio: ")
        if not precio.isdigit():
            print("Error: ingrese número")

    precio = int(precio)

    desc = ""
    while desc.lower() not in ["s", "n"]:
        desc = input("¿Descuento (S/N)?: ")
        if desc.lower() not in ["s", "n"]:
            print("Error: solo S o N")

    total_sin += precio

    if desc.lower() == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con += precio_desc

ahorro = total_sin - total_con
promedio = total_con / cantidad

print(f"Total sin descuentos: ${total_sin}")
print(f"Total con descuentos: ${total_con:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")