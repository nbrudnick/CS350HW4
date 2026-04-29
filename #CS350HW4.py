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
        temp_tri = test_input[i]
        my_sum = short_path_tab(temp_tri, temp_tri)
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

def short_path_tab(t_tri, tri):#solution #3
    #t_tri = true triangle, original data
    #tri = triangle, we update this with shortest path as we go
    #h = hieght
    #k = width
    h = 2#start at second to last layer

    while h >= 0:#loop through and do all the work once
        k = 0
        while k != -1 and k < 3:#while there is data and we are in range
            left = tri[h+1][k]
            right = tri[h+1][k+1]
            if tri[h][k] == t_tri[h][k]:#check if work needs to be done
                if left < right:
                    tri[h][k] += tri[h+1][k]#update tri with shortest path
                else:
                    tri[h][k] += tri[h+1][k+1]#update tri with shortest path
            k += 1
        h -= 1
    return tri[0][0]#return shortest path

def short_path_memoize_wrap(t_tri, tri):#solution #2
    #t_tri = true triangle, original data
    #tri = triangle, we update this with shortest path as we go
    h = 0 #hight
    k = 0 #width
    return short_path_memoize(t_tri, tri, h, k)

def short_path_memoize(t_tri, tri, h, k):#solution #2
    #t_tri = true triangle, original data
    #tri = triangle, we update this with shortest path as we go
    if h > 3 or k < 0:#base case out of range
        return 0
    
    if h == 3:#base case max hieght
        return tri[h][k]
    
    if tri[h][k] != t_tri[h][k]:#check if work to be done
        return tri[h][k]#early return if work already done
    
    if tri[h+1][k] != -1:
        left = short_path_memoize(t_tri, tri, h+1, k)

    if tri[h+1][k+1] != -1:
        right = short_path_memoize(t_tri, tri, h+1, k+1)

    if left < right:
        tri[h][k] += left#update tri with work completed
        return tri[h][k]
    else:
        tri[h][k] += right#update tri with work completed
        return tri[h][k]

def short_path_naive_wrap(tri):#solution #1
    h = 0 #hight
    k = 0 #width
    return short_path_naive(tri, h, k)

def short_path_naive(tri, h, k):#solution #1
    if h > 3 or k < 0:
        return 0
    
    if h == 3:
        return tri[h][k]
    
    if tri[h+1][k] != -1:
        left = short_path_naive(tri, h+1, k)

    if tri[h+1][k+1] != -1:
        right = short_path_naive(tri, h+1, k+1)

    if left < right:
        return left + tri[h][k]
    else:
        return right + tri[h][k]

if __name__ == "__main__":
    main()