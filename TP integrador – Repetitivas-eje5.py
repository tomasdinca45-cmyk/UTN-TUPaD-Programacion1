nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo letras")

vida_j = 100
vida_e = 100
pociones = 3
ataque = 15
ataque_e = 12

while vida_j > 0 and vida_e > 0:
    print(f"\n{nombre} HP:{vida_j} vs Enemigo HP:{vida_e} | Pociones:{pociones}")
    print("1.Ataque 2.Ráfaga 3.Curar")

    op = input("Opción: ")

    if not op.isdigit():
        print("Error")
        continue

    op = int(op)

    if op < 1 or op > 3:
        print("Error")
        continue

    if op == 1:
        if vida_e < 20:
            daño = ataque * 1.5
        else:
            daño = ataque

        vida_e -= daño
        print(f"Daño: {daño}")

    elif op == 2:
        for i in range(3):
            vida_e -= 5
            print("Golpe por 5")

    elif op == 3:
        if pociones > 0:
            vida_j += 30
            pociones -= 1
        else:
            print("Sin pociones")

    if vida_e > 0:
        vida_j -= ataque_e
        print("Enemigo ataca por 12")

if vida_j > 0:
    print("VICTORIA")
else:
    print("DERROTA")