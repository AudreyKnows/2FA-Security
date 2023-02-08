import time
import pyotp

key = ("NeuralNineMySuperSecretKey")
totp= pyotp.TOTP(key)
print(totp.now())