import random
import string


def generate_random_mobile_number():
    mobile_length = 10  # Change this to the desired length of the mobile number
    random_digits = '6'  # Start with "6"
    random_digits += ''.join(random.choices(string.digits, k=mobile_length - 1))  # Generate the remaining digits
    return random_digits


def generate_random_otp():
    otp_length = 6  # Change this to the desired OTP length
    return ''.join(random.choices(string.digits, k=otp_length))
