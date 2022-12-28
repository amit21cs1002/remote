import qrcode as qr 

try:
  img=qr.make("merry christmas")
  img.save("helloqr.png")
except:
                    print("Error")

