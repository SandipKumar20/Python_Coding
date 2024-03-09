pw = input("Enter a new password: ")


def password_check(password):
    results = {}
    if len(password) >= 8:
        results['length'] = True
    else:
        results['length'] = False

    digit = False

    for k in password:
        if k.isdigit():
            digit = True

    results['digits'] = digit

    uppercase = False

    for t in password:
        if t.isupper():
            uppercase = True

    results['upper_case'] = uppercase

    if all(results.values()):
        return "The password is strong!"
    else:
        return "The password is weak!"


result = password_check(pw)
print(result)