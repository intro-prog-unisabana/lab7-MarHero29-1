filename = input("Enter the CSV file name:\n")
import password_manager


def main():
    

    
    password_manager.encrypt_passwords_in_file(filename)

    
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input().strip()

        
        if option == "1":
            data = input("Enter the website and the new password:\n").split()

            if len(data) < 2:
                print("Input is in the wrong format!")
                continue

            website, new_password = data[0], data[1]

            if len(new_password) < 12:
                print("Password is too short!")
                continue

            result = password_manager.change_password(filename, website, new_password)

            if not result:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")

        
        elif option == "2":
            data = input("Enter the website, username, and password:\n").split()

            if len(data) < 3:
                print("Input is in the wrong format!")
                continue

            website, username, password = data[0], data[1], data[2]

            if len(password) < 12:
                print("Password is too short!")
                continue

            password_manager.add_login(filename, website, username, password)
            print("Login added.")

        
        elif option == "3":
            break

        
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()
