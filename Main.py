arrNum = [7, 9, 3, 5, 2, 6, 5, 4, 6, 1, 6, 3, 7, 5, 8, 3, 1, 2, 8, 9]
arrOdd = []
arrEven = []
print("Welcome, to the 499 Git Exercise!")
<<<<<<< HEAD
print(" ")
print("We will extract the odd and even numbers and putting them into two separate arrays.")
print(" ")
print("Each array will be sorted (both the even and the odd)")
print(" ")
=======
print("We will extract the odd and even numbers and putting them into two separate arrays./n")
>>>>>>> master

for num in arrNum:
    if num%2 == 0:
        arrEven.append(num)
<<<<<<< HEAD
        arrEven.sort()

for num in arrNum:
    if num%2 != 0:
        arrOdd.append(num)
        arrOdd.sort()
arrNum.sort()

print("Original Array (sorted): ", arrNum)
print("Even array (sorted): ", arrEven)
print("Odd array (sorted): ", arrOdd)
print(" ")
print("Done!")
=======
    if num%2 != 0:
        arrOdd.append(num)


print(arrNum)
print(arrEven)
print(arrOdd)



>>>>>>> master

