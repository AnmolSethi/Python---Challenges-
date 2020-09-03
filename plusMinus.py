N = int(input())
A = list(map(int, input().split()))

positiveNumbers = list(filter(lambda x: x >= 1, A))
negitiveNumber = list(filter(lambda x: x < 0, A))
zeroNumber = list(filter(lambda x: x == 0, A))

print(round(float(len(positiveNumbers) / N), 6))
print(round(float(len(negitiveNumber) / N), 6))
print(round(float(len(zeroNumber) / N), 6))