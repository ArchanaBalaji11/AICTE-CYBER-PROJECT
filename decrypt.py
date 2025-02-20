import cv2

# Load Encrypted Image
img = cv2.imread("Encryptedmsg.png")  # Ensure PNG is used

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Load Saved Password & Message Length
try:
    with open("pw.txt", "r") as file:
        saved_password = file.read().strip()

    with open("length.txt", "r") as file:
        msg_length = int(file.read().strip())

except FileNotFoundError:
    print("Required files not found! Encryption might not have been performed.")
    exit()

# Character Mapping for Decryption
c = {i: chr(i) for i in range(256)}

# Password Verification
pas = input("Enter passcode for decryption: ")

if saved_password == pas:
    message = ""
    n, m = 0, 0

    for _ in range(msg_length):  # Read only the correct message length
        value = img[n, m, 0]  # Read from Blue channel
        char = c.get(value, "?")  # Default to '?' if value is invalid
        message += char

        print(f"Retrieving: {value} -> {char} at ({n}, {m})")  # Debugging

        m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
            if n == img.shape[0]:
                break

    print("\nDecrypted message:", message)
else:
    print("Invalid passcode! Access denied.")
