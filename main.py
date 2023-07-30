import smtplib

import random


def generate_otp():

return str(random.randint(100000, 999999))


def send_otp_email(receiver_email, otp):

sender_email = 'yourmail@gmail.com' # Replace with your Gmail email address

sender_password = 'your app password' # Replace with your Gmail password or app password

subject = 'OTP Verification'

body = f'Your OTP is: {otp}'


message = f'Subject: {subject}\n\n{body}'


try:

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(sender_email, sender_password)

server.sendmail(sender_email, receiver_email, message)

print("OTP sent successfully!")

server.quit()

except Exception as e:

print(f"Error sending email: {e}")


def verify_otp(otp, entered_otp):

return otp == entered_otp


if _name_ == "_main_":

# Step 1: Generate OTP

otp = generate_otp()


# Step 2: Get the user's email address

receiver_email = input("Enter your email address: ")


# Step 3: Send OTP via email

send_otp_email(receiver_email, otp)


# Step 4: Simulate the user entering the OTP

entered_otp = input("Enter the OTP received in your email: ")


# Step 5: Verify OTP

if verify_otp(otp, entered_otp):

print("OTP verification successful.")

else:

print("OTP verification failed.")