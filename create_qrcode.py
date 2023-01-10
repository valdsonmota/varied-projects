import pyqrcode
import png
from pyqrcode import QRCode

#Link para criação do QRCode
QRString = 'https://drive.google.com/file/d/1Vf80rFpFY9KO9Y-eC1Q0qOJHlJF01Y3x/view?usp=share_link'

#Geração do QRCode
url = pyqrcode.create(QRString)

#Salva o QRCode gerado
url.png(r'qr.png', scale=8)
