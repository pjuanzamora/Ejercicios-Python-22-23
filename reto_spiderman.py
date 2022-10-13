#Ayudar a Spiderman a saber la ruta mas corta 
#El programa tiene que saber la distancia total recorrida

puntoA = int(input("Dime el punto A: "))
puntoB = int(input("Dime el punto B: "))

rutaA = puntoA + (puntoB - puntoA)
print(f"Ruta A cuesta {rutaA}")
rutaB = puntoB + abs(puntoA - puntoB)
print(f"Ruta B cuesta {rutaB}")

if (rutaA < rutaB):
    print(f"La mejor ruta es la A y cuesta {rutaA}km")
else:
    print(f"La mejor ruta es la B y cuesta {rutaB}km")