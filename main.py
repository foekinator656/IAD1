from week1.SelectionSort import *


if __name__ == '__main__':
    usersInput = input("What's the value you want to multiple, divide or constantly add up to?: ")
    usersInputAmountOfTimes = input("How many times do you want it to be divided, multiplied or added up to?: ")
    constant_linear_kwadratisch_kubisch_logarithmisch(usersInput, usersInputAmountOfTimes)
    recursive(int(usersInput), int(usersInputAmountOfTimes))
    exponentialRecursive(int(usersInput), int(usersInputAmountOfTimes))
