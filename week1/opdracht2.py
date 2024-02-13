# Opdracht 2
def constant_linear_kwadratisch_kubisch_logarithmisch(usersInput, usersInputAmountOfTimes):
    usersInputInInteger = int(usersInput)

    print("Constant: " + usersInput)

    for value in range(int(usersInputAmountOfTimes)):
        newValue = usersInputInInteger * value
        print("Linear: " + str(newValue))
        for value2 in range(int(usersInputAmountOfTimes)):
            newValue2 = value * value2
            print("Kwadritisch: " + str(newValue2))
            for value3 in range(int(usersInputAmountOfTimes)):
                newValue3 = value2 * value3
                print("Kubisch: " + str(newValue3))

    for value in range(int(usersInputAmountOfTimes)):
        newValue = value * 2
        print("Logarithmisch: " + str(newValue))

def recursive(usersInput, usersInputAmountOfTimes):
    if usersInput < int(usersInputAmountOfTimes):
        usersInput = usersInput * usersInput
        recursive(usersInput, usersInputAmountOfTimes)

    print("Recursion is the next: " + str(usersInput))

def exponentialRecursive(usersInput, usersInputAmountOfTimes):
    if usersInput < usersInputAmountOfTimes:
        usersInput = usersInput * usersInput
        recursive(usersInput, usersInputAmountOfTimes)
        recursive(usersInput, usersInputAmountOfTimes)

    print("Recursion is the next: " + str(usersInput))


