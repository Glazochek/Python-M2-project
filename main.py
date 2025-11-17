"""

This file for main actions

"""
from validation import check_email


def main():
    email = input("Please enter your email: ")
    if not check_email(email):
        print("Invalid email, you will not see my beautiful 3D animation in console.")
        return



if __name__ == "__main__":
    main()
