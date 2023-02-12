import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://drive.google.com/file/d/1Z0P1hN-vfpWmXVvJNrJ3whq87YNWvujg/view?usp=share_link'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'qr.png', scale=8)
