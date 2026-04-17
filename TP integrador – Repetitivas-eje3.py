# espacios
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

nombre_op = ""
while not nombre_op.isalpha():
    nombre_op = input("Nombre operador: ")

salir = False

while not salir:
    print("\n1.Reservar 2.Cancelar 3.Ver día 4.Resumen 5.Salir")
    op = input("Opción: ")

    if not op.isdigit():
        print("Error")
        continue

    op = int(op)

    if op == 1:
        dia = input("Día (1=Lunes 2=Martes): ")
        if not dia.isdigit():
            continue

        dia = int(dia)

        nombre = ""
        while not nombre.isalpha():
            nombre = input("Nombre paciente: ")

        if dia == 1:
            if nombre in [lunes1, lunes2, lunes3, lunes4]:
                print("Repetido")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Sin cupo")

        elif dia == 2:
            if nombre in [martes1, martes2, martes3]:
                print("Repetido")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("Sin cupo")

    elif op == 2:
        dia = input("Día: ")
        nombre = input("Nombre: ")

        if dia == "1":
            if lunes1 == nombre: lunes1 = ""
            elif lunes2 == nombre: lunes2 = ""
            elif lunes3 == nombre: lunes3 = ""
            elif lunes4 == nombre: lunes4 = ""
        elif dia == "2":
            if martes1 == nombre: martes1 = ""
            elif martes2 == nombre: martes2 = ""
            elif martes3 == nombre: martes3 = ""

    elif op == 3:
        dia = input("Día: ")

        if dia == "1":
            print("Lunes:", lunes1 or "libre", lunes2 or "libre", lunes3 or "libre", lunes4 or "libre")
        elif dia == "2":
            print("Martes:", martes1 or "libre", martes2 or "libre", martes3 or "libre")

    elif op == 4:
        ocup_lunes = sum([lunes1!="", lunes2!="", lunes3!="", lunes4!=""])
        ocup_martes = sum([martes1!="", martes2!="", martes3!=""])

        print("Lunes:", ocup_lunes, "ocupados")
        print("Martes:", ocup_martes, "ocupados")

    elif op == 5:
        salir = True