import string

password = str("~~")
cracked = [33]
if password == "":
    print("Password has been cracked\n"
          "Password: ")
else:
    x = 34
    j = 0
    guess = ''
    while password != guess:
        guess = ''
        if x == 127:
            cracked[j] = 33
            if j< 1:
                cracked.append(33)
                j+=1
            if cracked[j-1]!= 127:
                cracked[j-1] +=1

            # for  n in range()
            x = 33
        cracked[j] = x
        for i in range(0,len(cracked)):
            guess = guess+str(chr(cracked[i]))
        print("guess = " + guess,
              "cracked = "+ str(cracked))
        x+=1
    print("password: " +guess)

