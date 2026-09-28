import random
import time

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]

    left=[]
    middle=[]
    right=[]

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    if k < len(left):
        return quickselect(left, k)

    elif k < len(left) + len(middle):
        return pivot

    else:
        return quickselect(right, k - len(left) - len(middle))

def quickselectmom(arr, k): #AI
    if len(arr) == 1:
        return arr[0]

    def median5(a, start, end):
        vals = a[start:end]

        if len(vals) == 1:
            return vals[0]

        if len(vals) == 2:
            return vals[0] if vals[0] > vals[1] else vals[1]

        if len(vals) == 3:
            a, b, c = vals
            if a < b:
                a, b = b, a
            if b < c:
                b = c
            return a if a < b else b

        if len(vals) == 4:
            a, b, c, d = vals

            if a < b:
                a, b = b, a
            if c < d:
                c, d = d, c

            if a < c:
                a, c = c, a
                b, d = d, b

            return b if b < c else c

        a, b, c, d, e = vals

        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c

        if b > d:
            b, d = d, b
            a, c = c, a

        if c > e:
            c, e = e, c

        if b > c:
            return c
        return b

    def median_of_medians(a):
        n = len(a)

        if n <= 5:
            return median5(a, 0, n)

        medians = []

        for i in range(0, n, 5):
            medians.append(median5(a, i, min(i + 5, n)))

        return median_of_medians(medians)

    pivot = median_of_medians(arr)

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    if k < len(left):
        return quickselect(left, k)

    if k < len(left) + len(middle):
        return pivot

    return quickselect(
        right,
        k - len(left) - len(middle)
    )


def quickselect_improved(arr, k):
    if len(arr) == 1:
        return arr[0]

    min=arr[0]
    max=arr[0]
    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x

    pivot = (max + min) // 2

    left=[]
    middle=[]
    right=[]

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    if k < len(left):
        return quickselect(left, k)

    elif k < len(left) + len(middle):
        return pivot

    else:
        return quickselect(right, k - len(left) - len(middle))

def diytest_recursive(data, offset, median_location): #Rekurzív
    min = data[0]
    max = data[0]
    for d in data:
        if d < min:
            min = d
        if d > max:
            max = d

    if min == max:
        return min

    middle = (max + min) / 2
    data_A = []
    data_B = []
    for d in data:
        if d <= middle:
            data_A.append(d)
        else:
            data_B.append(d)

    if offset + len(data_A) > median_location:
        return diytest_recursive(data_A, offset, median_location)
    else:
        return diytest_recursive(data_B, offset + len(data_A) , median_location)

length = 1000001
iterations = 100
target = (length-1)//2
numbers = [
    [random.randint(1, length * 10)  for _ in range(length)]
    for _ in range(iterations)
]

start = time.perf_counter()
for i in range(0, iterations):
    diytest_recursive(numbers[i], 0, target)
end = time.perf_counter()
print("Diy Recursive: " + str(end-start))

start = time.perf_counter()
for i in range(0, iterations):
    quickselect_improved(numbers[i], target)
end = time.perf_counter()
print("Quickselect improved: " + str(end-start))

start = time.perf_counter()
for i in range(0, iterations):
    quickselect(numbers[i], target)
end = time.perf_counter()
print("Quickselect: " + str(end-start))

start = time.perf_counter()
for i in range(0, iterations):
    quickselect(numbers[i], target)
end = time.perf_counter()
print("Quickselect w/ MoM: " + str(end-start))
