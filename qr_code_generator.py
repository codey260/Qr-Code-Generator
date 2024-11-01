# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# Declaring The Variable Which Represents To Url, Text Or Phone Number
text = input("Type In URL or Text: ").strip()

# Making The Qr Code
qrcode = pyqrcode.create(text)

# Saving The QrCode In File Named "MyQrcode.png"
qrcode.png("MyQrcode.png", scale=20)

# Printing Message To The User
print("Qr Code Made Successfully")
