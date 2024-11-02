password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

# Check if digit is in string

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digit"] = digit

# Check is uppercase character is in string

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Uppercase"] = uppercase

print(result)
if all(result.values()):
    print('Strong Password')
else:
    print("Weak Password")
