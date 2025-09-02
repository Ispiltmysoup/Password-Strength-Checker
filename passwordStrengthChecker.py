password = str("K!elkow1cz")

index = int(0)
strength = 0

for chr in password:
    asciiValue = ord(password[index])
    index+=1
    if asciiValue == 32:
        print("Spaces are not allowed")
    elif 97 <= asciiValue <123:
        strength+=1
    elif 65<= asciiValue <91:
        strength +=1.5
    elif 48 <= asciiValue < 58:
        strength +=2
    else:
        strength +=3
print(strength)