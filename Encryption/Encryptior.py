class Encryptior:
    @staticmethod
    def encrypt_and_decrypt(text, key):
        return [chr(ord(char) ^ key) for char in text]

if __name__ == "__main__":
    encrypt = Encryptior.encrypt_and_decrypt("מה נשמע", 50)
    print(Encryptior.encrypt_and_decrypt(encrypt, 50))