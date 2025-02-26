import string
import getpass

def check_password():
    password = getpass.getpass("Please Enter Your password")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "very bad password || change password"
    elif strength == 2:
        remarks = "not a good password || change ASAP"
    elif strength == 3:
        remarks = "it is a weak password, consider changing"
    elif strength == 4:
        remarks = "it is a hard password, can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print("Your password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    
    print(f"Password strength: {strength}")
    print(f"Hint: {remarks}")

def ask_password(another_password=False):
    valid = False
    while not valid:
        if another_password:
            choice = input('Do you want to change your password (y/n)? ')
        else:
            choice = input("Do you want to check password (y/n)? ")

        if choice.lower() == 'y':
            valid = True
            return True
        elif choice.lower() == 'n':
            valid = True
            return False
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    print("++ Welcome to Password Checker ++")
    ask = ask_password()

    while ask:
        check_password()
        ask = ask_password(True)
