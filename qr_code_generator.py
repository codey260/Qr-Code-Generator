# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# Declaring The Variable Which Represents To Url, Text Or Phone Number
text = "https://www.github.com/youcefshaaban"

# Making The Qr Code
qrcode = pyqrcode.create(text)

# Saving The QrCode In File Named "MyQrcode.png"
qrcode.png("MyQrcode.png", scale=100)
