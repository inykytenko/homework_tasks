password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigigt():
        digit = True
result.append(digit)

uppercase = False
for i in password:
    if i.isupper()
        uppercase = True

result.append(digit)
print(result)

