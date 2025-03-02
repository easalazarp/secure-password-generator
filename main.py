import re
import secrets
import string

from tabulate import tabulate
from dbconecction import DBConection

RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Validar que se ingrese una loginitud correcta
def password_length():
    length = 0
    while True:
        try:
            print("Por favor ingrese la longitud con un mínimo de 8 y máximo 16 caracteres")
            length = int(input("Longitud: "))
            if 8 <= length <= 16:
                break
            else:
                print("*** Ingrese una número entre 8 a 16 ***")
        except ValueError:
            print("*** Ingrese un número entre 8 a 16 ***")

    return length

# Validar que solo se puedan agregar opciones disponibles
def add_characters():
    character = 0
    while True:
        try:
            print("¿Qué caracteres desea agregar?")
            print("(1) Números (2) Caracteres especiales (3) Números y caracteres especiales (4) Ninguno")
            character = int(input("Ingrese una opción: "))
            if 1 <= character <= 4:
                break
            else:
                print("*** Debe seleccionar al menos una opción válida ***")
        except ValueError:
            print("*** Ingrese una opción válida ***")
    return character


def password_generator():
    letters = string.ascii_letters
    length = password_length()
    character = add_characters()

    match character:
        case 1:
            letters += string.digits
        case 2:
            letters += string.punctuation
        case 3:
            letters += string.digits + string.punctuation
        case 4:
            letters = letters
    secure_password = ''.join(secrets.choice(letters) for _ in range(length))
    print("---------------------------------------------------------------------")
    print(f"[ Contraseña segura: {secure_password} ]")
    print("---------------------------------------------------------------------")
    print(f"Fuerza de la contraseña: {password_strength_meter(secure_password)}")
    print("---------------------------------------------------------------------")
    print("**********************************************************************")
    return secure_password


def processed_password():
    except_activated = False
    # Controla si el usuario requiere regenerar nuevamente una contraseña
    while True:
        try:
            # except_activated  controla que solo llama a esta función cuando ingrese
            # por primer vez o cuando el usuario quiere generar otra contraseña
            if not except_activated:
                password = password_generator()
                save_password(password)
            print("Desea generar otra contraseña:")
            print("(1) Generarar otra contraseña (2) Menú (0) Salir")
            option = int(input("Ingrese una opción: "))
            if  option == 1:
                except_activated = False
                continue
            elif option == 2:
                main_menu()
                break
            elif option == 0:
                return
            else:
                print("**** Ingrese una opción válida****")
                except_activated = True
        except ValueError:
            except_activated = True

# Medidor de fuerza de contraseña
def password_strength_meter(password):

    score = 0
    # Criterio de fortaleza
    if len(password) >= 8:
        score += 1

    # Verificar mayusculas
    if re.search("[a-z]", password):
        score += 1

    # Verificar minusculas
    if re.search("[a-z]", password):
        score += 1

    # Verficar numeros
    if re.search("[0-9]", password):
        score += 1

    # Verificar caracteres especiales
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Verificar longitud adicional
    if len(password) >= 12:
        score += 1

    # Clasificion de la fortaleza por puntos
    if score <= 2:
        show_progress_bar(score)
        return f"{RED}Débil{RESET}"
    elif score <= 4:
        show_progress_bar(score)
        return f"{YELLOW}Media{RESET}"
    elif score <= 5:
        show_progress_bar(5)
        return f"{GREEN}Fuerte{RESET}"
    else:
        show_progress_bar(score)
        return f"{GREEN}Muy Fuerte{RESET}"

#Mostrar medidor de fuerza de contraseña
def show_progress_bar(score):
    percent = round((score * 10) / 6)
    show_percent = round((score * 100) / 6)
    bar = "="
    bar_residue = "="
    color = ""
    RED = "\033[31m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    residue = 6 - score

    for i in range(percent):
        bar += "="

    if residue > 0:
        for i in range(residue):
            bar_residue += "="
    else:
        bar_residue = ""

    if score <= 2:
        color = RED
    elif score <= 4:
        color = YELLOW
    elif score <= 5:
        color = GREEN
    else:
        color = GREEN

    print(f"[ {color}{bar}{RESET}{bar_residue} ] {color}{percent*10}%{RESET}")

# Guardar contraseña en base de datos
def save_password(password):

    while True:
        print("¿Desea guardar la contraseña? (S/N)")
        option = str(input("Ingrese una opción: "))
        if option == 'S' or option == 's':
            break
        elif option == 'N' or option == 'n':
            return


    while True:
        name = input("Ingrese el nombre del registro: ")
        if len(name) > 0:
            break

    reference = input("Ingrese la url (no abligatorio): ") or '--'
    DBConection.save_password(name,reference,password)

# Mostrar contraseñas desde base de datos
def show_password_list():
    password_list = DBConection.get_password()
    header = ["ID","Name","Url","Password"]
    table = []
    if len(password_list) > 0:
        for item in password_list:
            table.append(item)
        print(tabulate(table,header,tablefmt="fancy_grid"))
        password_list_menu()
    print("-------------------------------------------------------")
    print("| No se encuentra ningun registro en la base de datos |")
    print("-------------------------------------------------------")
    main_menu()

def password_list_menu():
    print("*** Opciones de registros ***")
    while True:
        try:
            print("(1) Modificar")
            print('(2) Eliminar')
            print('(3) Menú principal')
            print('(4) Salir')

            value = int(input("Seleccione una opción: "))
            if value == 1:
                modify_password()
                break
            elif value == 2:
                confirm_delete()
                break
            elif value == 3:
                main_menu()
            elif value == 4:
                return
        except ValueError:
            print("**** Ingrese una opción válida****")

def modify_password():
    print("*** Modificar registro ***")
    while True:
        try:
            id_reference = int(input("Ingrese el ID del registro a modificar: "))
            name = input("Ingrese el nuevo nombre del registro: ")
            url = input("Ingrese la nueva url (no abligatorio): ") or '--'
            DBConection.update_name_and_reference(id_reference,name,url)
            break
        except ValueError:
            print(f"{RED}Ingrese un ID válido{RESET}")

    show_password_list()

def confirm_delete():
    while True:
        try:
            print('¿Está seguro de eliminar el registro? (S/N)')
            option = str(input("Ingrese una opción: "))
            if option == 'S' or option == 's':
                delete_password()
                break
            elif option == 'N' or option == 'n':
                show_password_list()
                break
        except ValueError:
            print(f"{RED}Ingrese una opción válida{RESET}")

def delete_password():
    while True:
        try:
            id_reference = int(input("Ingrese el ID del registro a eliminar: "))
            DBConection.register_delete(id_reference)
            break
        except ValueError:
            print(f"{RED}Ingrese un ID válido{RESET}")

    show_password_list()

def main_menu():
    print("*** Bienvenido al Generador de contraseñas seguras ***")
    while True:
        try:
            print("(1) Generar contraseña")
            print("(2) Ver contraseñas guardadas")
            print("(0) Salir")
            value = int(input("Seleccione una opción: "))
            if value == 1:
                processed_password()
                break
            elif value == 2:
                show_password_list()
                break
            elif value == 0:
                break
            else:
                print("*** Debe seleccionar al menos una opción válida ***")
        except ValueError:
            print("*** Ingrese una opción válida ***")




if __name__ == "__main__":
    DBConection()
    main_menu()
