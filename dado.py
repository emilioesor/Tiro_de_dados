import random

respuesta = "y"

while respuesta == "y":
    print("Tirando el dado...")
    numero = random.randint(1, 6)
    print("El dado muestra:", numero)

    

    if respuesta != "y":
        print("¡Hasta luego!")

    # dados icon
    if numero == 1:
        print("░░░░░░░░░░")
        print("░░░░░░░░░░")
        print("░░░░▓▓░░░░")
        print("░░░░░░░░░░")
        print("░░░░░░░░░░")

    elif numero == 2:
        print("░░░░░░░░░░")
        print("░░░░░░▓▓░░")
        print("░░░░░░░░░░")
        print("░░▓▓░░░░░░")
        print("░░░░░░░░░░")

    elif numero == 3:
        print("░░░░░░░░░░")
        print("░░░░░░░▓▓░")
        print("░░░░▓▓░░░░")
        print("░▓▓░░░░░░░")
        print("░░░░░░░░░░")

    elif numero == 4:
        print("░░░░░░░░░░")
        print("░░▓▓░░▓▓░░")
        print("░░░░░░░░░░")
        print("░░▓▓░░▓▓░░")
        print("░░░░░░░░░░")

    elif numero == 5:
        print("░░░░░░░░░░")
        print("░▓▓░░░░▓▓░")
        print("░░░░▓▓░░░░")
        print("░▓▓░░░░▓▓░")
        print("░░░░░░░░░░")

    elif numero == 6:
        print("░░░░░░░░░░")
        print("░░▓▓░░▓▓░░")
        print("░░▓▓░░▓▓░░")
        print("░░▓▓░░▓▓░░")
        print("░░░░░░░░░░")

    respuesta = input("¿Quieres tirar el dado de nuevo? (y/n): ")