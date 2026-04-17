def caesar_encrypt(text):
    result = ""

    for char in text:
        # Letras
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))

        # Números
        elif char.isdigit():
            result += str((int(char) + 3) % 10)

        # Símbolos (no cambian)
        else:
            result += char

    return result
    main()