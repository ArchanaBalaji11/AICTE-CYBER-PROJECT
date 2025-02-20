# AICTE-CYBER-PROJECT
📌 Project Overview
 Image-Based Steganography Using Python .This project implements Image Steganography, a technique that allows hiding secret messages inside an image by modifying its pixel values. The hidden message can later be retrieved using the correct password.
⚙ Project Workflow
🔹 1. Encryption (Hiding a Secret Message)
The user inputs a secret message and a password.
The message length and password are stored in separate text files (length.txt, pw.txt).
Each character in the message is converted into its ASCII value and stored inside an image’s pixel values.
The modified image is saved as Encryptedmsg.png and displayed.
🔹 2. Decryption (Retrieving the Secret Message)
The user enters the passcode.
The program verifies the saved password.
The pixel values are extracted and converted back into characters.
If the correct password is entered, the original message is displayed.
📥 Installation Guide
🔧 Prerequisites
Make sure you have Python 3+ installed. You can check your version using:
python --version
📦 Required Libraries
Before running the project, install the required libraries:
pip install opencv-python
If you encounter issues, you may also need:
pip install numpy
🚀 How to Use
🔹 Step 1: Encrypt a Message
Run the encryption script:
python encrypt.py
Enter your secret message and password.
The encrypted image (Encryptedmsg.png) is generated.
🔹 Step 2: Decrypt the Message
Run the decryption script:
python decrypt.py
Enter the correct password.
The hidden message is retrieved and displayed.
📁 Project Structure
/image-steganography
│── encrypt.py          # Encrypts message into an image
│── decrypt.py          # Decrypts the hidden message
│── Encryptedmsg.png    # Image with hidden message
│── pw.txt              # Stores encryption password
│── length.txt          # Stores message length
│── README.md           # Documentation
⚠ Troubleshooting
Issue: Decryption outputs random characters.
Solution: Ensure you're using PNG format (JPG compression corrupts pixel data).
Issue: Incorrect password always results in access denied.
Solution: Ensure pw.txt is correctly generated after encryption.
📜 License
This project is open-source under the MIT License. Feel free to use and modify it!
