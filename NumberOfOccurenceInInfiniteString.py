S, N = input().strip(), int(input().strip())
print(S.count("a") * (N // len(S)) + S[:N % len(S)].count("a"))