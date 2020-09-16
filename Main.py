import unittest

arrNum = [7, 9, 3, 5, 2, 6, 5, 4, 6, 1, 6, 3, 7, 5, 8, 3, 1, 2, 8, 9]
arrOdd = []
arrEven = []
print("Welcome, to the 499 Git Exercise!")
print("We will extract the odd and even numbers and putting them into two separate arrays.")
print("Each array will be sorted (both the even and the odd)")

for num in arrNum:
    if num%2 != 0:
        arrOdd.append(num)
        arrOdd.sort()
arrNum.sort()

class testOdd(unittest.TestCase):
    def test2(self):
        self.assertEqual(arrOdd, [1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 9, 9])

print("Original Array (sorted): ", arrNum)
print("Odd array (sorted): ", arrOdd)
print("Done!")

if __name__ == '__main__':
    unittest.main()