# Generates a QR code
# https://github.com/lincolnloop/python-qrcode
# get <"pip install qrcode"> in terminal first 

import os
import qrcode

# Generate QR code
link = str(input("Digite o link para gerar o qrcode: "))
img = qrcode.make(f"{link}")

# Save file
img.save("qrcode.png", "PNG")

# Open file
os.system("open qrcode.png")
