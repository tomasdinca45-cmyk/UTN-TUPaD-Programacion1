usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    usuario = input(f"Intento {intentos+1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada")
else:
    salir = False
    while not salir:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
        elif opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirm = input("Confirmar clave: ")
                if nueva == confirm:
                    clave_correcta = nueva
                    print("Clave cambiada.")
                else:
                    print("Error: no coinciden.")
        elif opcion == 3:
            print("¡Seguí adelante, vos podés!")
        elif opcion == 4:
            salir = True