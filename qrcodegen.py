import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# data that will be changed into QRCode
data = "Rndom"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
# create and adding QRCode
qr.add_data(data)
img = qrcode.make(fit=True)
# changing default QRCode to red color
qr.make_image(fill_color="red", back_color="white")
img.save("C:/Users/Admin/OneDrive/Документы/QRCode/myqrcode.png")
# decoding QRCode
de = Image.open("C:/Users/Admin/OneDrive/Документы/QRCode/myqrcode.png")
result = decode(de)

print(result)
