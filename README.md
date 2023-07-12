# Cryptography-using-QR-encyption

Prototype:
- Introduction:
  - Generate a QR code with an encrypted message.
  - Scanning the QR code redirects to a website for decryption.

- Encryption:
  - Use Fernet encryption algorithm for message security.

- QR Code Generation:
  - Utilize qrcode library to generate QR codes.
  - Parameters for version, box size, and border.

- Message Encryption:
  - Encrypt message using Fernet cipher.
  - Convert encrypted message to URL-safe format.

- Website Redirection:
  - QR code redirects to "https://retail.onlinesbi.sbi/retail/login.htm".
  - Decrypt encrypted message on the website.

- Conclusion:
  - Securely transmit encrypted data via QR codes.
  - Enhance communication and data privacy.
 
Algorithm:

1. Generate a new encryption key using the Fernet algorithm.
2. Create a Fernet cipher instance using the generated key.
3. Encrypt the desired message using the Fernet cipher.
4. Convert the encrypted message to URL-safe format.
5. Generate a QR code using the qrcode library with the URL-safe encrypted message.
6. Save the QR code image.
7. Display or distribute the QR code for scanning.
8. When the QR code is scanned:
   - Redirect to the specified website, e.g., "https://retail.onlinesbi.sbi/retail/login.htm".
   - Retrieve the encrypted message from the URL parameter.
   - Use the Fernet cipher with the encryption key to decrypt the message.
9. Perform any necessary actions with the decrypted message.

Output:
![image](https://github.com/Rishima15/Cryptography-using-QR-encyption/assets/90675961/13d9ec5f-d3d1-4377-8757-2554b1f6a718)

Which will Lead to:
![image](https://github.com/Rishima15/Cryptography-using-QR-encyption/assets/90675961/ac8de8e9-68a9-455b-81c1-136812476047)


