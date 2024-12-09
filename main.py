
import os
import time
from truco_parcial import Mazo, Player

def guardar_historial(texto):
    with open("historial.txt", "a") as archivo:
        archivo.write(texto + "\n")

nombre_jugador = input("Ingresa tu nombre: ")
mazo = Mazo()

p1 = Player(nombre_jugador)
p2 = Player("Profe")



while True:
    os.system("clear")
    
    print(f"{p1.nombre} tiene {p1.puntos} puntos")
    print(f"{p2.nombre} tiene {p2.puntos} puntos")
    print("")

    guardar_historial(f"{p1.nombre} tiene {p1.puntos} puntos")
    guardar_historial(f"{p2.nombre} tiene {p2.puntos} puntos")

    
    p1.mano = []
    p2.mano = []

    for i in range(3):
        p1.agarrar_carta(mazo.agarrar())
        p2.agarrar_carta(mazo.agarrar())

    ganador = False
    ronda = 1
    
    p1.primera = False
    p2.primera = False

    while ronda <= 3 and ganador == False:
        print(f"Ronda {ronda}")
        guardar_historial(f"Ronda {ronda}")

        p1.jugar_carta()
        print(f"{p1.nombre} - juega {p1.carta_jugada.mostrar()}")
        time.sleep(3)
        print("")

        p2.jugar_carta()
        print(f"{p2.nombre} - juega {p2.carta_jugada.mostrar()}")
        time.sleep(3)
        print("")
        print("")
        
        
        if p1.carta_jugada.valor > p2.carta_jugada.valor:
            print(f"{p1.nombre} gana el turno")
            guardar_historial(f"{p1.nombre} gana el turno")
            if p1.primera:
                print(f"gano {p1.nombre}!")
                guardar_historial(f"¡Ganó {p1.nombre}!")
                ganador = True
                
            else:
                p1.primera = True
            
            if p1.primera:
                    print(f"{p1.nombre} gano la mano!")
                    guardar_historial(f"{p1.nombre} ganó la mano!")
                    p1.puntos += 1 
            else:
                p1.primera = True

        elif p1.carta_jugada.valor < p2.carta_jugada.valor:
            print(f"{p2.nombre} gana el turno")
            guardar_historial(f"{p2.nombre} gana el turno")
            paux = p2
            p2 = p1
            p1 = paux

            if p1.primera:
                    print(f"{p1.nombre} gano la mano!")
                    guardar_historial(f"{p1.nombre} ganó la mano!")
                    p1.puntos += 1
            else:
                p1.primera = True
        else:
            print("Empate parda la mejor!")
            guardar_historial("Empate, ¡parda la mejor!")

        time.sleep(3)
        ronda += 1


