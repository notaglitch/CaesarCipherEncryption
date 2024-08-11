alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
  print(''' 

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌               ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌               ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                              

''')
  print("This tool is using encryption method of 'Caesar cipher'. ")
  print("*********************Made for PRACTICE*********************")
  while True:
    choice = input("Type 'encode' to Encrypt and 'decode' to Decrypt. ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if choice == "encode":
        encrypt(text, shift)
    elif choice == "decode":
        decrypt(text, shift)
    else:
        print("Please give a valid input \n ")
    continue

def encrypt(original_text, shift_amount):
  cipher_text = ""
  for letter in original_text:
    shifted_position = alphabet.index(letter) + shift_amount
    shifted_position %= len(alphabet)
    cipher_text += alphabet[shifted_position]
  print(f"Here is the encode message '{cipher_text}'. ")

def decrypt(original_text, shift_amount):
  cipher_text = ""
  for letter in original_text:
    shifted_position = alphabet.index(letter) - shift_amount
    shifted_position %= len(alphabet)
    cipher_text += alphabet[shifted_position]
  print(f"The decoded message is ==> {cipher_text}. ")

if __name__ == "__main__":
    main()

