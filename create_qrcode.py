import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://valdsonmota.github.io/projeto-site-portfolio/pages/python-studies.html'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'QR-Code_06-2023.png', scale=8)
