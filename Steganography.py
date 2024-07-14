import cv2
import os
import hashlib 
image_path = r""C:\Users\megha\OneDrive\Pictures\nature.jpeg"" 
img = cv2.imread(image_path)
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

height, width, channels = img.shape
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()
d = {}
c = {}
for i in range(256):
    d[chr(i)] = i   
    c[i] = chr(i)  

n = 0  
m = 0 
z = 0

# Encode the secret message into the image using the hashed password
for i in range(len(msg)):
    
    new_value = (int(img[n, m, z]) + d[msg[i]] + hashed_password[i % len(hashed_password)]) % 256
    img[n, m, z] = new_value
    
    m += 1
    if m >= width:
        m = 0
        n += 1
    if n >= height:
        print("Image too small to hold the entire message.")
        break
    
    # Cycle through the color channels (0, 1, 2) for RGB
    z = (z + 1) % 3
encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
cv2.imwrite(encrypted_image_path, img)
os.startfile(encrypted_image_path)

print(f"Message has been encoded into '{encrypted_image_path}'.")               