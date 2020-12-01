import sys
def challenge1():
 with open("inputs.txt") as inputNumbers:
    inputs = [line.rstrip() for line in inputNumbers]
    for x in inputs:
     newX = int(x)
     for y in inputs:
            newY = int(y)
            year = newX+newY
            if year == 2020:
             print(newY*newX)


def challenge2():
    with open("inputs.txt") as inputNumbers:
        inputs = [line.rstrip() for line in inputNumbers]
        for x in inputs:
            newX = int(x)
            for y in inputs:
                newY = int(y)
                for z in inputs:
                    newZ = int(z)
                    year = newX + newY + newZ
                    if year == 2020:
                        print(newY * newX * newZ)

challenge1()
print("Next Challenge:")
challenge2()
