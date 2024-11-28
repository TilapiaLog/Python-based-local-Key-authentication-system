from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from AES import AESCipher

class LoginSystem:
    def __init__(self, aes_cipher, keyword, iv):
        self.aes_cipher = aes_cipher
        self.keyword = keyword
        self.iv = iv

    def login(self, ciphertext):
        """尝试登录，检查明文中是否包含关键词"""
        try:
            plaintext = self.aes_cipher.decrypt(ciphertext, self.iv)
            if self.keyword in plaintext:
                return "Login successful"
            else:
                return "Login failed"
        except Exception as e:
            return f"The key format is incorrect"


def main():
    key = "Test"
    keyword = "FuDie" 
    iv = "28baad78be5165f4231fac05453addb7"
    aes_cipher = AESCipher(key)


    ciphertext = input("Please enter a key: ")


    login_system = LoginSystem(aes_cipher, keyword, iv)

   
    result = login_system.login(ciphertext)
    print(result)  

if __name__ == "__main__":
    main()