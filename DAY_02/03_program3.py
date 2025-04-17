# Fibonacci series
num = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b
