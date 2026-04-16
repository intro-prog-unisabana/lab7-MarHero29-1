import csv
from caesar import caesar_encrypt


def encrypt_single_pass(filename):
    with open(filename, 'r') as file:
        password = file.read().strip()

    encrypted = caesar_encrypt(password)

    with open(filename, 'w') as file:
        file.write(encrypted)


def encrypt_passwords_in_file(filename):
    rows = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)

    for i in range(1, len(rows)):
        rows[i][2] = caesar_encrypt(rows[i][2])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def change_password(filename, website, password):
    rows = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)

    for i in range(1, len(rows)):
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)

            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            return True

    return False


def add_login(filename, website_name, username, password):
    encrypted = caesar_encrypt(password)

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted])