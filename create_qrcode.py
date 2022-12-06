import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'http://www.valdson.com'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'qr.png', scale=8)
