DB = []


def agregarUsuario(DB):
    print("## Crear Usuario ##")
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    user = {"username": usuario, "password": contrasena}
    DB.append(user)


def iniciarSesion(DB):
    print("## Iniciar Sesion ##")
    usuario = input("Ingresar usuario: ")

    for user in DB:
        if user["username"] == usuario:
            contrasena = input("Ingresar contraseña: ")
        else:
            print("# Usuario no encotrado #")
            break
        if user["password"] == contrasena:
            print("# Sesion iniciada con éxito #")
            break
        else:
            print("# Contraseña Incorrecta #")
            break


def consultarDB(DB):
    if len(DB) == 0:
        print(
            "# La base de datos se encuentra vacia actualmente debes crear al menos 1 usuario#"
        )
    for user in DB:
        print("## Base de datos de Usuarios ##")
        print(f'Usuario: {user["username"]}, Contraseña: {user["password"]}')


def guardarDB(DB):
    with open("Practica1/db.txt", "w") as file:
        for user in DB:
            file.write(f'Usuario: {user["username"]}, Contraseña: {user["password"]}\n')


def App(DB):
    print("### Elige una de las siguientes opciones: ###")
    print("# 1. Crear Usuario")
    print("# 2. Consultar Base de Datos")
    print("# 3. Guardar BD en un Archivo")
    print("# 4. Cerrar Aplicación")
    if len(DB) != 0:
        print("# 5. Iniciar Sesión")
    option = input("Número de opción: ")
    if option == "1":
        agregarUsuario(DB)
        App(DB)
    elif option == "2":
        consultarDB(DB)
    elif option == "3":
        guardarDB(DB)
    elif option == "4":
        print("### App cerrada con éxito ###")
        return
    elif option == "5":
        iniciarSesion(DB)
    else: 
        print("### Opción Inválida ###")
    App(DB)


App(DB)
