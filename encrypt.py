import cv2
import os

# Load Image (Ensure it's PNG)
img = cv2.imread("ak.png")  # Ensure it's a PNG image

# Secret Message Input
msg = input("Enter secret message: ")
password = input("Enter password: ")

# Save Password & Message Length
with open("pw.txt", "w") as file:
    file.write(password)

with open("length.txt", "w") as file:
    file.write(str(len(msg)))

# Character to Byte Mapping
d = {chr(i): i for i in range(256)}

# Encryption Process (Modify Only Blue Channel)
n, m = 0, 0
for char in msg:
    img[n, m, 0] = d[char]  # Store in the Blue channel
    print(f"Storing: {char} -> {d[char]} at ({n}, {m})")  # Debugging
    m += 1
    if m == img.shape[1]:  
        m = 0
        n += 1
        if n == img.shape[0]:  
            break

# Save Encrypted Image
cv2.imwrite("Encryptedmsg.png", img)
os.system("start Encryptedmsg.png")
print("Encryption successful! Image saved as 'Encryptedmsg.png'.")


