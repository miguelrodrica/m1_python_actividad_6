import csv

def validate_login(email, password):
    with open("m1_python_actividad_6/login.csv","r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if email == fila[1] and password == fila[2]:
                validate = True
                break
            elif email != fila[1] or password != fila[2]:
                validate = False
                continue
    return validate

def menu_crud():
    while True:
        print("\033[95m\nMENÚ CRUD DE USUARIOS\033[0m")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario por correo")
        print("4. Eliminar usuario")
        print("5. Buscar usuario por correo")
        print("6. Salir")
        try:
            choice = int(input("\nSeleccione una opción: "))
            if choice <= 0 or choice > 6:
                print("\033[91m\n¡ERROR!. Número no contemplado en la lista.\033[0m")
            else:
                break
        except ValueError:
            print("\033[91m\n¡ERROR! Debe escribir un número, intente nuevamente.\033[0m")
    return choice

def create_user():
    name = input("\nNombres: ")
    last_name = input("Apellidos: ")
    email = input("Correo: ").lower()
    with open("m1_python_actividad_6/usuarios.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([name, last_name, email])
        print("\033[92m\n¡Usuario creado exitosamente!\033[0m")

def show_users():
    with open("m1_python_actividad_6/usuarios.csv", "r", newline="") as archivo:
        reader = csv.reader(archivo)
        filas = list(reader)
        if len(filas) == 0:
            print("\033[93m\n¡VACÍO! Aún no se registra ningún usuario.\033[0m")
        else:
            print("\n")
            for fila in filas:
                print(f"\033[96mNombre: {fila[0]} | Apellidos: {fila[1]} | Correo: {fila[2]}\033[0m")

def update_user():
    while True:
        email_user = input("\nEmail del usuario a actualizar: ").lower()
        validate = False
        with open("m1_python_actividad_6/usuarios.csv", "r", newline="") as archivo:
            reader = csv.reader(archivo)
            filas = list(reader)
        for fila in filas:
            if email_user == fila[2]:
                print("\033[95m\nEscriba los datosa a actualizar\033[0m")
                new_name = input("Nuevo nombre: ")
                new_last_name = input("Nuevos apellidos: ")
                new_email = input("Nuevo correo: ").lower()
                fila[0] = new_name
                fila[1] = new_last_name
                fila[2] = new_email
                validate = True
                break
        if validate == False:
            print("\033[91m\n¡ERROR! El email no se relaciona a ningún usuario.\033[0m")
            continue
        with open("m1_python_actividad_6/usuarios.csv", "w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerows(filas)
        print("\033[92m\nUsuario actualizado correctamente.\033[0m")
        break

def delete_user():
    repeat = True
    while repeat:
        email_user = input("\nEmail del usuario a eliminar: ").lower()
        with open("m1_python_actividad_6/usuarios.csv", "r", newline="") as archivo:
            reader = csv.reader(archivo)
            filas = list(reader)
        for fila in filas:
            if email_user == fila[2]:
                filas.remove(fila)
                print("\033[92m\nUsuario eliminado satisfactoriamente.\033[0m")
                with open("m1_python_actividad_6/usuarios.csv", "w", newline="") as archivo:
                    writer = csv.writer(archivo)
                    writer.writerows(filas)
                repeat = False
                break
        if email_user != fila[2]:
            print("\033[91m\n¡ERROR! El email no se relaciona a ningún usuario.\033[0m")
            continue

def search_user():
    repeat = True
    while repeat:
        email_user = input("\nEmail del usuario a buscar: ").lower()
        with open("m1_python_actividad_6/usuarios.csv", "r", newline="") as archivo:
            reader = csv.reader(archivo)
            filas = list(reader)
        for fila in filas:
            if email_user == fila[2]:
                print(f"\033[92m\nNombre: {fila[0]} | Apellidos: {fila[1]} | Email: {fila[2]}\033[0m")
                repeat = False
                break
        if email_user != fila[2]:
            print("\033[91m\n¡ERROR! El email no se relaciona a ningún usuario.\033[0m")
            continue
