# #class of January 14th, 2025
#First name
# Last name
# Email Address
# Phone Number
# Job Title
# ID Number
print("I'm going to make an ID for you!")
print("I'm going to ask you a few questions though: ")
first = input("Your first name please: ")
last = input("Your last name: ")
email = input("Now email: ")
phone = input("phone number: ")
job = input("Job Title! ")
id = input("Your ID number: ")
hair = input("Your hair color: ")
eye = input("color of your eye: ")
training = input("Do you have training? yes/no: ")
month = input("What month did you start: ")


print("-----------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job.title())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair.capitalize()}       Eyes: {eye.capitalize()}")
print(f"Month: {month.capitalize()}      Training: {training.capitalize()}")
print("-----------------------")