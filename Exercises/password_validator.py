
password = input()

# check that the password may not contain the keywords password or 123456
if "password" in password or "123456" in password:
    print("The password may not contain the keywords “password” or “123456”.")
# check that the password may start with the keyword qwerty
elif password.startswith("qwerty"):
    print("The password may not start with the keyword “qwerty” but it may contain it.")
# check that the password must at least one non-alphabetic character (i.e. numbers or special characters)
elif not any(char.isalpha() for char in password):
    print("The password must contain at least one non-digit character.")
elif not any(char.isdigit() for char in password):
    print("The password must contain at least one non-alphabetic character.")
elif not any(("$" in char or "@" in char or "!" in char) for char in password):
    print("The password must contain at least one of the following special characters: $, @ or !.")
elif not any((char.isupper() for char in password) and (char.islower() for char in password)):
    print("The password must have both uppercase and lowercase letters.")
else:
    print("The password is valid!")

