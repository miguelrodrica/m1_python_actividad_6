import csv
from funciones import *

repeat = True
while repeat:
    print("\033[95m\nLOGIN\033[0m")
    email = input("Correo: ").lower()
    password = input("Contraseña: ").lower()

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
            elif choice == 4:
                delete_user()
            elif choice == 5:
                search_user()
            else:
                print("\033[93m\n¡Bye!\033[0m")
                repeat = False
                break
    elif validate == False:
        print("\033[91m\n¡ERROR! Correo o contraseña son incorrectos, intente nuevamente.\033[0m")
    
    else:
        repeat = False
