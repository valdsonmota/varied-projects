import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://drive.google.com/file/d/1fC8l6PTXg-gMV9P7IBuvJIetshHrD7l2/view?usp=sharing'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'QR-Code_06-2023.png', scale=8)
