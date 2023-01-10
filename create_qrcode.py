import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://drive.google.com/file/d/1XFZPF1vxBW-wMxPsirUNrbW73fpAoBI2/view?usp=share_link'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'qr.png', scale=8)
