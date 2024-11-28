from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from AES import AESCipher
from StateMonitor import GlobalVarMonitor
import random

monitor = GlobalVarMonitor()
isSuccessd = monitor()  # Create a global variable in the monitor
monitor.set_var(isSuccessd, False)  # Initialize it to False

class LoginSystem:
    def __init__(self, aes_cipher, keyword, iv):
        self.aes_cipher = aes_cipher
        self.keyword = keyword
        self.iv = iv

    def login(self, ciphertext):
        """Attempt to log in by checking if the plaintext contains the keyword."""
        try:
            plaintext = self.aes_cipher.decrypt(ciphertext, self.iv)
            if self.keyword in plaintext:
                monitor.set_var(isSuccessd, True)  # Set the variable to True in the monitor
                print("Login successful")
                # Check the value from the monitor
                if monitor.get_var(isSuccessd):  # Get the value from the monitor
                    self.start_guessing_game()  # Start the guessing game upon successful login
                else:
                    print("Login failed")
                return "Login successful"
            else:
                return "Login failed"
        except Exception as e:
            return f"The key format is incorrect: {e}"

    def start_guessing_game(self):
        """Start the guessing game."""
        number_to_guess = random.randint(1, 100)
        attempts = 0
        print("Welcome to the guessing game! Please guess a number between 1 and 100.")

        while True:
            guess = input("Enter your guess: ")
            attempts += 1
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Please ensure your guess is between 1 and 100.")
                    continue
                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed it right, the number is {number_to_guess}. You took {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input, please enter a number.")

def main():
    key = "FuDie"
    keyword = "Test" 
    iv = "d06c4855b1c2e7d400ee38009e725d70"
    aes_cipher = AESCipher(key)

    ciphertext = input("Please enter a key: ")

    login_system = LoginSystem(aes_cipher, keyword, iv)

    result = login_system.login(ciphertext)
    print(result)  

if __name__ == "__main__":
    main()