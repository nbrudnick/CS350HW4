#CS350HW3
#Nikki Rudnick, 4/7/2026
#PSU CS350 
#shortest path triangle

'''Constraints:

    Assume all test case triangles will have a base of size 4 (like the example image above)
    Assume all test cases will be represented in code as a 4x4, 2-dimensional matrix 
    Assume all numbers represented in the triangle are positive integers
    Solution #1 must be recursive and not utilize dynamic programming
    Solution #2 must be recursive and utilize dynamic programming, specifically Memoization
    Solution #3 must be iterative and utilize dynamic programming, specifically Tabulation
'''

def main(): 
    tri1 = [ 
        [2, -1, -1, -1],
        [5, 4, -1, -1],
        [1, 4, 7, -1],
        [8, 6, 9, 6],
    ]
    tri2 = [
        [4, -1, -1, -1],
        [4, 4, -1, -1],
        [4, 4, 4, -1],
        [4, 4, 4, 4,],
    ]
    tri3 = [
        [6, -1, -1, -1],
        [2, 1, -1, -1],
        [4, 1, 1, -1],
        [1, 10, 9, 6],
    ]
    tri4 = [
        [3, -1, -1, -1],
        [2, 4, -1, -1],
        [7, 2, 1, -1],
        [4, 10, 1, 6],
    ]

    test_input = [tri1, tri2, tri3 ,tri4]
    test_ans = [
        [2, 5, 1, 6],
        [4, 4, 4, 4],
        [6, 2, 4, 1],
        [3, 2, 2, 1],
    ]

    i = 0
    for row in test_ans:

        print("test triangle", i, ":", test_input[i])
        temp = []
        my_sum = short_path_naive_wrap(test_input[i], temp)
        print("shortest sum path", i, ":", temp)
        print("shortest sum", i, ":", my_sum)

        print("correct shortest sum path", i, ":", row)
        good_sum = sum(row)
        print("correct shortest sum", i, ":", good_sum)
        if temp == row and sum == good_sum:
            print("GOOD")
        else:
            print("BAD")
        i = i+1
    return

#c(n,k) = c(n-1, k-1) + c(n-1, k)
#base cases: 
# k == 1 --> n
# k == n --> 1

def short_path_naive_wrap(tri, temp):
    h = 0 #hight
    k = 0 #width
    return short_path_naive(tri, temp, h, k)

def short_path_naive(tri, temp, h, k):
    if h > 3 or k < 0:
        return 0
    
    if h == 3:
        return tri[h][k]
    
    if tri[h+1][k] != -1:
        left = short_path_naive(tri, temp, h+1, k)

    if tri[h+1][k+1] != -1:
        right = short_path_naive(tri, temp, h+1, k+1)

    if left < right:
        temp.append(tri[h+1][k])
        return left + tri[h][k]
    else:
        temp.append(tri[h+1][k+1])
        return right + tri[h][k]
        
    

'''def nchoose_naive(n, k):
    if k == 1:
        return n
    if n == 1:
        return 1
    if k == n:
        return 1
    
    #left child includes apples
    #right child excludes apples
    ans = nchoosek_naive(n-1, k-1) + nchoosek_naive(n-1, k)
    return ans

def nchoosek_memo(n,k, table):
    if k == 1:
        table[n][k] = n
        return n
    if k == n:
        table[n][k] = 1
        return 1
    if table[n][k] != -1:
        #someone else answered it
        return table[n][k]

    #do the work
    ans = nchoosek_naive(n-1,k-1) + nchoosek_naive(n-1,k)
    #add ans to the table
    table[n][k] = ans
    return ans

def main():
    n = 5
    k = 3

    table = [[-1]*(k+1) for _ in range(n+1)] #builds the table rows n, cols k
    print(nchoosek_memo(n,k, table))'''

if __name__ == "__main__":
    main()