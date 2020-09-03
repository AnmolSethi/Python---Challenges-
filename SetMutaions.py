input()
A = set(map(int, input().split()))

for _ in range(int(input())):
    cmd = input().split()
    B = set(map(int, input().split()))
    getattr(A, cmd[0])(*[B])
print(sum(A))