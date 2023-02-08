import time
import pyotp 
key = ("NeuralNineMySuperSecretKey")
counter = 0
hotp =pyotp.HOTP(key)
print(hotp.at(0))
      

