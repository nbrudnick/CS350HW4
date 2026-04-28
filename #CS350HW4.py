#CS350HW3
#Nikki Rudnick, 4/7/2026
#PSU CS350 
#mergesort

def main(): 
    test_input = [
        [[1,2,4,5], [2,3,4,5,6]],
        [[1,1,1], [1,1]],
        [[], [1,2,3]],
        [[], []],
        [[1,3,5], [2,4,6,7,8,9]],
        [[1,2,3], [4,5,6]],
        [[4,5,6], [1,2]],
        [[1,2,2,3], [2,3,4,4,4]],
        [[0,5,10,56,60,100,200], [2,3,10,60,70,80,200,500]]
        ]

    test_ans = [
       [1,2,3,4,5,6],
       [1],
       [1,2,3],
       [],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6],
       [1,2,4,5,6],
       [1,2,3,4],
       [0,2,3,5,10,56,60,70,80,100,200,500]
    ]

    i = 0
    for row in test_input:

        print("test array(s) set", i, ":", row[0], row[1])
        temp = mergesort_wrapper(row[0], row[1])
        print("sorted list", i, ":", temp)
        print("correct sorted list", i, ":", test_ans[i])
        if temp == test_ans[i]:
            print("GOOD")
        else:
            print("BAD")
        i = i+1
    return

def mergesort_wrapper(arr_a, arr_b):

    array = arr_a + arr_b

    start = 0
    end = len(array) - 1

    mergesort(array, start, end)
    remove_dup(array)
    return array

def remove_dup(array):
    i = 0
    while i < len(array):
        if array[i] == array[(i-1)]:
            del array[i]
            i -= 1
        i += 1


def mergesort(array, start, end):
    if start >= end:
        #empty child
        #or a single element
        return

    mid = (start + end) //2

    #left child
    mergesort(array, start, mid)
    #right child
    mergesort(array, mid+1, end)

    #the work! merge both kids so they are sorted
    merge(array, start, mid, end)

def merge(array, start, mid, end):
    temp = []
    #left child iterator start-mid
    a = start
    #right child interator mid+1-end
    b = mid+1
    #loop comparing what a is looking at against what b is looking at
    #choose the smaller, and append it to temp
    while a <= mid and b <= end:
        if array[a] < array[b]:
            temp.append(array[a])
            a += 1
        else:
            temp.append(array[b])
            b += 1
    #if a's sub array still has data to put into temp
    while a <= mid: 
        temp.append(array[a])
        a += 1
    #if b's sub array still has data to put into temp
    while b <= end:
        temp.append(array[b])
        b += 1
    
    i = 0#temp interator
    cur = start #array interator
    while i < len(temp):
        array[cur] = temp[i]
        i += 1
        cur += 1
    


if __name__ == "__main__":
    main()