usuSecreto = "juan"
passSecreto = "12"

usuario = input("Dime tu ususario: ")
password = input("Dime tu contraseña: ")

while (usuSecreto!=usuario or passSecreto!=password):
    if (usuSecreto!=usuario):
        print("Error en el usuario")
        usuario = input("Dime tu ususario: ")
    elif (passSecreto!=password):
        print("Error en el password")
        password = input("Dime tu password: ")
    


print("Usuario y password correcto")