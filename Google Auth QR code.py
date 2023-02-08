import time
import qrcode
import pyotp
key = ("NeuralNineMySuperSecretKey")
counter = 0

uri = pyotp.totp.TOTP(key).provisioning_uri(name="AudreyG123",

            issuer_name= "NeuralNine App")
qrcode.make(uri).save("totp.png")
print(uri)
