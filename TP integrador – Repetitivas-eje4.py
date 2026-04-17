energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo = ""
racha = 0

nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre agente: ")

while energia > 0 and tiempo > 0 and cerraduras < 3:
    print(f"\nEnergía:{energia} Tiempo:{tiempo} Cerraduras:{cerraduras}")

    op = input("1.Forzar 2.Hackear 3.Descansar: ")

    if not op.isdigit():
        continue

    op = int(op)

    if op == 1:
        energia -= 20
        tiempo -= 2
        racha += 1

        if racha == 3:
            alarma = True
            print("Alarma activada por spam")
            racha = 0
            continue

        if energia < 40:
            num = input("Riesgo (1-3): ")
            if num == "3":
                alarma = True

        if not alarma:
            cerraduras += 1

    elif op == 2:
        energia -= 10
        tiempo -= 3
        racha = 0

        for i in range(4):
            codigo += "A"

        if len(codigo) >= 8 and cerraduras < 3:
            cerraduras += 1

    elif op == 3:
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        racha = 0
        if alarma:
            energia -= 10

    if alarma and tiempo <= 3:
        print("Bloqueo por alarma")
        break

if cerraduras == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")