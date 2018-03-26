# https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
#subset sum problem is a NP-complete problem
#but we can solve the problem in Pseudo-polynomial time using Dynamic programming

#code
def sss(l, n, t):
    if t==0: return True
    if n==0: return False
    if l[n-1] > t: return sss(l[:-1], n-1, t)
    return sss(l[:-1], n-1, t-l[-1]) or sss(l[:-1], n-1, t)

def sss1(l, t):
    if t % 1: return False
    dp = [[False] * int(t+1) for i in range(len(l)+1)]
    for i in range(len(l)+1):
        dp[i][0] = True
    for i in range(1,len(l)+1):
        for j in range(1,int(t)+1):
            if i > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-l[i-1]]
    return dp[-1][-1]

print(sss1([1,5,11,5], 11))
print(sss1([1,3,5], 4.5))
#tests = int(input())
#for i in range(tests):
#    length = int(input())
#    l = input().split()
#    l = list(map(int, l))
#    s = sum(l)
#    if sss1(l, s/2):
#        print('YES')
#    else:
#        print('NO')