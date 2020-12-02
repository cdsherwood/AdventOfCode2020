

def challenge1():
    goodPasswords = 0
    with open("inputs.txt") as inputs:
        passwords = [line.rstrip() for line in inputs]
        for password in passwords:
            passwordThings = password.split(" ")
            limit = passwordThings[0]
            letter = passwordThings[1]
            passphrase = passwordThings[2]
            limits = limit.split("-")
            limitMin = int(limits[0])
            limitMax = int(limits[1])
            occurence = 0
            for charachter in passphrase:
                if charachter == letter[0]:
                    occurence = occurence + 1
            if occurence >= limitMin:
                if occurence <= limitMax:
                    goodPasswords += 1
    print(goodPasswords)

def challenge2():
    goodPasswords = 0
    with open("inputs.txt") as inputs:
        passwords = [line.rstrip() for line in inputs]
        for password in passwords:
            passwordThings = password.split(" ")
            limit = passwordThings[0]
            letter = passwordThings[1]
            passphrase = passwordThings[2]
            limits = limit.split("-")
            limitOne = int(limits[0]) - 1
            limitTwo = int(limits[1]) - 1
            occurence = 0
            if passphrase[limitOne] == letter[0]:
                occurence = occurence + 1
            if passphrase[limitTwo] == letter[0]:
                occurence = occurence + 1
            if occurence == 1:
                goodPasswords += 1
    print(goodPasswords)


challenge1()
challenge2()
