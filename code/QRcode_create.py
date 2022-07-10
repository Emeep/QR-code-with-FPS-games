import qrcode as qr

name = 'hi, why did you scan this'

code = qr.make(name)
code.save("D:\\important shit\\Python shit\\QRcode gaming\\codes\\" + name + ".png")