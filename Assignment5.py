numbersInList = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbersInList.append(number)

sumOfNumbers = sum(numbersInList)
print("Sum of numbers in list: ", sumOfNumbers)

minNumber = min(numbersInList)
print("Smallest: ", minNumber)

maxNumber = max(numbersInList)
print("Largest: ", maxNumber)

ascending = sorted(numbersInList)
print("Ascending order: ", ascending)

descending = sorted(numbersInList, reverse = True)
print("Descending order: ", descending)

numbersInList_tuple = tuple(numbersInList)
print("Tuple: ", numbersInList_tuple)

del numbersInList
print("List deleted.")