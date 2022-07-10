import qrcode as qr

name = '' # text in qr code

code = qr.make(name)
code.save("(directory)" + name + ".png")
