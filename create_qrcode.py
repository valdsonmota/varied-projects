import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://drive.google.com/file/d/1bib0SvuNPUVjUF403e88TeNFeiNfANvv/view?usp=share_link'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'qr.png', scale=8)
