vowels = ["a","e","i","o","u"]
def check_vowel():
    letter = input("Enter any character: ")
    if letter in vowels:
        print("True")
    else:
        print("False")
check_vowel()
