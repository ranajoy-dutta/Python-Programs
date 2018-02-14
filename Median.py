def findMedian(a):
    a = sorted(a)
    if len(a)%2 == 0:
        return (a[int(len(a)/2)-1]+a[int((len(a)/2))])
    else:
        return (a[int((len(a))/2)])

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = findMedian(arr)
print(result)

