key = ("NeuralNineMySuperSecretKey")
totp= pyotp.TOTP(key)
print(totp.now())