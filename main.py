import string
import random

# Main function
if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Getting password length from user
    while True:
        try:
            passwordLength = int(input("Enter length of password you want: "))
            break
        except ValueError:
            print("Not a valid input! Try again.")

    conc = []
    conc.extend(list(s1))
    conc.extend(list(s2))
    conc.extend(list(s3))
    conc.extend(list(s4))

    # Select and print the password
    print("Your Password is: " + "".join(random.sample(conc, passwordLength)))
