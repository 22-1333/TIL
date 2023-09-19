import math
N = int(input())
max_a = N // 1
max_b = N // 2
max_c = N // 3
count = 0

for a in range(max_a + 1):
    for b in range(max_b + 1):
        for c in range(max_c + 1):
            if a * 1 + b * 2 + c * 3 == N:
                count += math.factorial(a + b + c) / (math.factorial(a) * math.factorial(b) * math.factorial(c))

print(int(count))
