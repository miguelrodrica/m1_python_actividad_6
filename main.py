import csv
from funciones import validate_login
from funciones import menu_crud
from funciones import create_user
from funciones import show_users
from funciones import update_user

while True:
    print("\033[95m\nLOGIN\033[0m")
    email = input("Correo: ")
    password = input("Contraseña: ")

    validate = validate_login(email, password)

    if validate == True: 
        print("\033[92m\nBienvenido, inició sesión correctamente.\033[0m")
        while True:
            choice = menu_crud()
            if choice == 1:
                create_user()
            elif choice == 2:
                show_users()
            elif choice == 3:
                update_user()
    else:
        print("\033[91m\n¡ERROR! Correo o contraseña son incorrectos, intente nuevamente.\033[0m")