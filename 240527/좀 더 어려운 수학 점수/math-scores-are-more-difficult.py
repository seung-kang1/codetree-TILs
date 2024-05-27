tmp1 = input()
arr1 = tmp1.split()
a = int(arr1[0])
b = int(arr1[1])

tmp2 = input()
arr2 = tmp2.split()
c = int(arr2[0])
d = int(arr2[1])

if a > c:
    print("A")
elif c > a:
    print("B")
elif a == c and b > d:
    print("A")
else:
    print("B")