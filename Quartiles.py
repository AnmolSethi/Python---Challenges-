N = int(input())
A = list(map(int, input().split()))

workingData = sorted(A, key=lambda x: x)
def odd_numbers():
    MEDIAN = N // 2
    LOWER_BOUND = (0, MEDIAN)
    UPPER_BOUND = (MEDIAN + 1, N)
    
    Q2 = workingData[MEDIAN]
    print(find_median(workingData[LOWER_BOUND[0]:LOWER_BOUND[1]]))
    print(Q2)
    print(find_median(workingData[UPPER_BOUND[0]:UPPER_BOUND[1]]))
    

def even_numbers():
    MEDIAN_L, MEDIAN_R = N // 2, (N // 2) - 1
    
    LOWER_BOUND = (0, MEDIAN_L)
    UPPER_BOUND = (MEDIAN_L, N)

    Q2 = (workingData[MEDIAN_L] + workingData[MEDIAN_R]) // 2
    print(find_median(workingData[LOWER_BOUND[0]:LOWER_BOUND[1]]))
    print(Q2)
    print(find_median(workingData[UPPER_BOUND[0]:UPPER_BOUND[1]]))
    
def find_median(data):
    ind1, ind2, n = 0, 0, len(data)
    if n % 2 == 0:
        ind1, ind2 = n // 2, (n // 2) - 1
        return (data[ind1] + data[ind2]) // 2
    else:
        ind1 = n // 2
        return data[ind1]
    
if N % 2 == 0:
    even_numbers()
else:
    odd_numbers()