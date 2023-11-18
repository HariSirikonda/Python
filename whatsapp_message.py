import pywhatkit

number = int(input("Enter the phone number : "))
hours = int(input("Enter the time of Hours in 24 hours format : "))
minutes = int(input("Enter the time in minutes : "))
message = input("Enter the Message : ")


if len(str(number))>10:
    print("Enter á valid phone number..!")
else:
    pass

phone_number = number
phone_number = str(phone_number)

pywhatkit.sendwhatmsg("+91"+phone_number, message, hours,minutes)
