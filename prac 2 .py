N = int(input())
L, W, K = map(int, input().split())

S = N * (2 * K + 2 * L) + W * N * (N + 1)

print(S)
