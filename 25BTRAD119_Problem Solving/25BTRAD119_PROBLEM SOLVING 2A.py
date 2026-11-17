import random

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

user = int(input("Enter OTP: "))

if user == otp:
    print("OTP Verified")
else:
    print("Invalid OTP")