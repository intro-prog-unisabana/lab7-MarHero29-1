import csv
from caesar import caesar_encrypt


def encrypt_single_pass(filename):
    # Leer solo la primera línea (la contraseña)
    with open(filename, 'r') as file:
        password = file.readline().strip()

    # Encriptar
    encrypted = caesar_encrypt(password)

    # Sobrescribir el archivo con la contraseña encriptada
    with open(filename, 'w') as file:
        file.write(encrypted)


def encrypt_passwords_in_file(filename):
    rows = []

    # Leer el archivo CSV
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # evitar filas vacías
                rows.append(row)

    # Encriptar solo la columna de contraseñas (índice 2), saltando encabezado
    for i in range(1, len(rows)):
        rows[i][2] = caesar_encrypt(rows[i][2])

    # Escribir de nuevo el archivo
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def change_password(filename, website, password):
    rows = []
    found = False

    # Leer el archivo
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)

    # Buscar y actualizar
    for i in range(1, len(rows)):
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)
            found = True
            break

    # Si no se encontró
    if not found:
        return False

    # Escribir cambios
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True


def add_login(filename, website_name, username, password):
    encrypted = caesar_encrypt(password)

    # Agregar nueva fila
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted])