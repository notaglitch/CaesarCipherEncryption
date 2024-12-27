# Caesar Cipher Encryption Tool

Welcome to the **Caesar Cipher Encryption Tool**! This simple tool allows you to encrypt and decrypt messages using the Caesar cipher technique, a basic form of encryption where each letter in the plaintext is shifted by a specified number of positions in the alphabet.

## Features
- **Encryption**: Input a message and a shift number to get the encrypted message.
- **Decryption**: Input an encrypted message and a shift number to retrieve the original plaintext message.
- **Shift Control**: You can adjust the number of shifts (or "key") to control how the cipher operates.
- **Simple User Interface**: Clear text-based prompts guide the user through the process.

---

## How to Use

1. **Clone the repository**:
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/notaglitch/caesar-cipher-tool.git
   ```

2. **Run the tool**:
   Navigate to the directory where the file is located and run the Python script:
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the prompts**:
   - The program will display an ASCII art header followed by a brief description of the tool.
   - You will be asked whether you want to **encode** (encrypt) or **decode** (decrypt) a message.
   - Enter your message and the shift number (an integer).
   - The tool will display the resulting encrypted or decrypted message.

4. **Example**:
   ```
   Type 'encode' to Encrypt and 'decode' to Decrypt. encode
   Type your message:
   hello
   Type the shift number:
   3
   Here is the encode message: khoor
   ```

---

## How the Caesar Cipher Works

The Caesar cipher is a substitution cipher in which each letter of the plaintext is shifted a certain number of positions down or up the alphabet. For example:
- Shift 1: 'a' becomes 'b', 'b' becomes 'c', ..., 'z' becomes 'a'.
- Shift 3: 'a' becomes 'd', 'b' becomes 'e', ..., 'z' becomes 'c'.

For decryption, the process is reversed: each letter of the ciphertext is shifted backwards by the specified shift number.

---

## Code Overview

The tool uses a list of lowercase alphabetic characters to perform encryption and decryption:

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

- **Encrypt function**: Takes the original message and shift number as inputs, shifts each letter in the message by the specified amount, and returns the resulting ciphered text.
- **Decrypt function**: Takes the ciphered text and shift number, reverses the shifting process, and returns the decoded message.

---

## Example Use Case

Let's say you want to encrypt the message "hello" with a shift of 3:

```
Input:
  Type 'encode' to Encrypt and 'decode' to Decrypt. encode
  Type your message:
  hello
  Type the shift number:
  3

Output:
  Here is the encode message: khoor
```

To decrypt the message "khoor" with a shift of 3:

```
Input:
  Type 'encode' to Encrypt and 'decode' to Decrypt. decode
  Type your message:
  khoor
  Type the shift number:
  3

Output:
  The decoded message is ==> hello.
```

---

## Requirements

- Python 3.x

---

## Contributing

Feel free to contribute by submitting issues or pull requests. If you find bugs or have ideas for new features, don't hesitate to open an issue.
