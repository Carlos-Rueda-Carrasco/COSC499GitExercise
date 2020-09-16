import unittest

#Author: Carlos
arrNum = [7, 9, 3, 5, 2, 6, 5, 4, 6, 1, 6, 3, 7, 5, 8, 3, 1, 2, 8, 9]
arrOdd = []
arrEven = []
print("Welcome, to the 499 Git Exercise!")
print(" ")
print("We will extract the odd and even numbers and putting them into two separate arrays.")
print(" ")
print("Each array will be sorted (both the even and the odd)")
print(" ")
print("We will extract the odd and even numbers and putting them into two separate arrays./n")

for num in arrNum:
    if num%2 == 0:
        arrEven.append(num)

        arrEven.sort()

class testEven(unittest.TestCase):
    def test1(self):
        self.assertEqual(arrEven, [2, 2, 4, 6, 6, 6, 8, 8])

for num in arrNum:
    if num%2 != 0:
        arrOdd.append(num)
        arrOdd.sort()
arrNum.sort()

class testOdd(unittest.TestCase):
    def test2(self):
        self.assertEqual(arrOdd, [1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 9, 9])

print("Original Array (sorted): ", arrNum)
print("Even array (sorted): ", arrEven)
print("Odd array (sorted): ", arrOdd)
print(" ")
print("Done!")

if __name__ == '__main__':
    unittest.main()
