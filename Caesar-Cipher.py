def encrypt(string: str, key: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    capital_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    for char in string:
        if char.isupper():
            cipher_text += capital_alpha[(int(capital_alpha.index(char)) + key) % 26]
        elif char.islower():
            cipher_text += alphabet[(int(alphabet.index(char)) + key) % 26]
        else:
            cipher_text += char
    return cipher_text

def decrypt(string: str, key: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    capital_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    for char in string:
        if char.isupper():
            cipher_text += capital_alpha[(int(capital_alpha.index(char)) - key) % 26]
        elif char.islower():
            cipher_text += alphabet[(int(alphabet.index(char)) - key) % 26]
        else:
            cipher_text += char
    return cipher_text

has_encrypted = False
if __name__ == '__main__':
    while True:
        try:
            print("1. Encrypt\n2. Decrypt") if has_encrypted is False else print("1. Encrypt\n2. Decrypt\n3. Decrypt last encrypted word")
            choice = int(input())
            if choice == 1:
                print("Enter your phrase: ")
                word = input()
                print("Enter a key: ")
                key = int(input())
                encrypted_word = encrypt(word, key)
                print(encrypted_word)
                has_encrypted = True
            elif choice == 2:
                print("Enter your phrase: ")
                word = input()
                print("Enter yor key: ")
                key = int(input())
                decrypted_word = decrypt(word, key)
                print(decrypted_word)
            elif choice == 3 and has_encrypted:
                print("Enter the key: ")
                key = int(input())
                print(decrypt(encrypted_word, key))
            else:
                print("Please choose from 1-3") if has_encrypted else print("Please choose from 1-2")
        except Exception as e:
            print(f"Error: {e}")


