#About the Code

#super basic QR genrator code

import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(version=1,error_correction=ERROR_CORRECT_L,box_size=20,border=1) #some settings of box size and border that i liked 

qr.add_data("Pretty cool stuff lol (:") #the text you want the QR code to have 
qr.make(fit=True)

img = qr.make_image(fill_color ="orange", back_color="black") #can play around with colors and see which suits you best
img.save("myqr.png") #name of the file in which genrated QR is getting saved
print("Done") 