arrNum = [7, 9, 3, 5, 2, 6, 5, 4, 6, 1, 6, 3, 7, 5, 8, 3, 1, 2, 8, 9]
arrOdd = []
arrEven = []
print("Welcome, to the 499 Git Exercise!")
print("We will extract the odd and even numbers and putting them into two separate arrays./n")

for num in arrNum:
    if num%2 == 0:
        arrEven.append(num)
    if num%2 != 0:
        arrOdd.append(num)


print(arrNum)
print(arrEven)
print(arrOdd)




