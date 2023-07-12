import os
import qrcode
from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Message to be encrypted and encoded in the QR code
message = "This is a secret message."

# Encrypt the message
encrypted_message = cipher_suite.encrypt(message.encode())

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(encrypted_message)
qr.make(fit=True)

# Specify the path to the desktop folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Save the QR code as an image file on the desktop
image_path = os.path.join(desktop_path, "encrypted_qrcode_downloads.png")
image = qr.make_image(fill_color="black", back_color="white")
image.save(image_path)
