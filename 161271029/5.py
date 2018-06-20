# 5

w = []
for i in range(50):
    w.append([0]*50)
#print(w)
a = []
dp = []
n = 0
m = 0
for i in range(50):
    dp.append([0]*50)

def main():
    inputVec = input().split()
    n, m = int(inputVec[0]), int(inputVec[1])
    inputVec = input().split()
    for i in range(n):
        a.append(int(inputVec[i]))
    init(a, n)
    print(proc())

def init(a, n):
    for i in range(n):
        for j in range(i+1, n):
            w[i][j] = w[i][j-1] + a[j] - a[(i+j)//2]

def proc():
    for i in range(n):
        dp[i][i] = 0
        dp[i][0] = w[0][i]
    for j in range(1, m):
        for i in range(j+1, n):
            dp[i][j] = 999
            for k in range(j-1, i):
                dp[i][j] = min(dp[i][j], dp[k][j-1] + w[k+1][i])
    return dp[n][m]



if __name__ == '__main__':
    main()