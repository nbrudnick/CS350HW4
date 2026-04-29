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

'''GOAL: find the shortest sum path from the top of the triangle to the bottom'''

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

        #print("test triangle", i, ":", test_input[i])
        #temp = []
        my_sum = short_path_tab_wrap(test_input[i])
        #print("shortest sum path", i, ":", temp)
        print("shortest sum", i, ":", my_sum)

        print("correct shortest sum path", i, ":", row)
        good_sum = sum(row)
        print("correct shortest sum", i, ":", good_sum)
        if my_sum == good_sum:
            print("GOOD")
        else:
            print("BAD")
        i = i+1
    return

def short_path_tab_wrap(tri):
    h = 2
    k = 0
    i = 0
    short_sum = 0
    cur_small = tri[h][k] + tri[h+1][k]

    while h < 3:
        while k != -2 and k < 4:
            left_small = tri[h][k] + tri[h+1][k]
            right_small = tri[h][k] + tri [h+1][k+1]
            if cur_small > left_small:
                cur_small = left_small
            if cur_small > right_small:
                cur_small = right_small
            k += 1
        h -= 1
    return

'''def short_path_tab_wrap_BAD(tri):
    h = 3
    i = 0
    temp_k = 0
    temp = tri[h][i]


#find the smallest number at the max hieght
    while i < 3:
        if tri[h][i] < temp:
            temp = tri[h][i]
            temp_k = i
        i += 1
    
    #add smalest number to short_sum
    short_sum = 0

    #starting from the smallest number at the base of the triangle, recurse up
    short_path_tab(tri, short_sum, h, temp_k)

    return short_sum

def short_path_tab_BAD(tri, short_sum, h, k):

    if tri[h][k] < 0:
        return 
    
    if k > 3:
        return
    
    if h == 0:
        short_sum += tri[h][k]
        return

    if tri[h-1][k] < tri[h-1][k+1]:
        short_sum += tri[h][k]
        short_path_tab(tri, short_sum, h-1, k)
    else:
        short_sum += tri[h][k]
        short_path_tab(tri, short_sum, h-1, k+1)'''


def short_path_memoize_wrap(tri):
    return

def short_path_memoize(tri, h, k):
    return

def short_path_naive_wrap(tri):
    h = 0 #hight
    k = 0 #width
    return short_path_naive(tri, h, k)

def short_path_naive(tri, h, k):
    if h > 3 or k < 0:
        return 0
    
    if h == 3:
        return tri[h][k]
    
    if tri[h+1][k] != -1:
        left = short_path_naive(tri, h+1, k)

    if tri[h+1][k+1] != -1:
        right = short_path_naive(tri, h+1, k+1)

    if left < right:
        #temp.append(tri[h+1][k])
        return left + tri[h][k]
    else:
        #temp.append(tri[h+1][k+1])
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