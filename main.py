from random import randint
import sys

def generateArrayOfIntegers():
    intArray = []
    for i in range(100):
        value = randint(0, 99)
        while(value in intArray):
            value = randint(0, 99)
        intArray.append(value)
    return intArray

def singleRun(iteration):
    found = True
    boxes = generateArrayOfIntegers()
    prisoners = generateArrayOfIntegers()

    for prisoner in prisoners:
        boxVal = boxes[prisoner]
        counter = 1
        while boxVal != prisoner and counter < 50:
            boxVal = boxes[boxVal]
            counter += 1
        if counter >= 50:
            found = False
    print("Iteration %s, Boxes Found? : %s" % (iteration, "Yes" if found else "No"))
    return found

if __name__ == "__main__":
    if not sys.argv[1]: sys.exit("No Iteration Number Specified!")
    foundCount = 0
    for i in range(int(sys.argv[1])):
        found = singleRun(i)
        if found: foundCount += 1
    print("Completed Iterations!")
    percentageFound = (foundCount / int(sys.argv[1])) * 100
    print("Percentage Found: %s%%" % (percentageFound))
