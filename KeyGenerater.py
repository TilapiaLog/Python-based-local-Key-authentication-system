from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
import random
import string
from AES import AESCipher

def generate_keys(keyword, count):
    texts = []
    keyword_length = len(keyword)
    
    for _ in range(count):
        if keyword_length >= 8:
            raise ValueError("To be on the safe side, keywords cannot be greater than or equal to 8 characters in length")
        
        random_letters_count = 20 - keyword_length
        random_letters = ''.join(random.choices(string.ascii_letters, k=random_letters_count))
        
        insert_position = random.randint(0, random_letters_count)
        
        text = random_letters[:insert_position] + keyword + random_letters[insert_position:]
        texts.append(text)
    
    return texts

def main():
    keyword = input("Please enter a keyword: ")
    count = int(input("Please enter the amount of generated key: "))
    key = input("Please enter the encryption key: ")
    output_file = input("Please enter the output file name (e.g. output.txt): ")

    try:
        texts = generate_keys(keyword, count)
    except ValueError as e:
        print(e)
        return
    

    aes_cipher = AESCipher(key)


    with open(output_file, 'w') as f:
        for i, text in enumerate(texts):
            ciphertext = aes_cipher.encrypt(text)
            f.write(f"Number {i + 1}:\n")
            f.write(f"Key: {ciphertext}\n\n")

    print(f"The encryption results have been exported to {output_file}")

    iv_hex = aes_cipher.iv.hex() 
    print(f"IV built into the main program: {iv_hex}") 

if __name__ == "__main__":
    main()