import os

password = str("~~!O")
cracked = [32]
if password == "":
    print("Password has been cracked\n"
          "Password: ")
else:
    j = 0
    guess = ''
    while password != guess:
        guess = ''
        # # if cracked[j] == 127:
        # #     cracked[j] = 33
        # #     # if j == 0:
        # #     #     cracked.append(32)
        # #     #     m = j
        # #     #     j+=1
        # #     if cracked[m]!= 127:
        # #         cracked[m] +=1
        # #     else:
        # #         cracked[m] = 33
        # #         cracked[m-1]+=1
        # for i in range(0, len(cracked)):
        #     if cracked[i] == 127:
        #         cracked[i] = 33
        #         yes = True
        #     else:
        #         yes = False
        # if yes == True:
        #     cracked.append(32)
        #     m = j
        #     j += 1
        if cracked[j] >= 127:
            if j ==0:
                cracked.append(32)
                cracked[j] = 33
                j+=1
            else:
                # if j <2:
                m = len(cracked)-1
                flag = False
                for int in reversed(cracked):
                    # print(cracked)
                    # print(m)
                    if cracked[m] >= 127:
                        cracked[m] = 32
                        cracked[m-1] +=1
                        flag = True
                        m-=1
                    else:
                        flag = False
                if flag == True:
                    cracked.append(32)
                    j+=1



        cracked[j]+=1
        # print(cracked)
        for i in range(0,len(cracked)):
            guess = guess+str(chr(cracked[i]))
        # print(guess)
    print("password: " +guess)

