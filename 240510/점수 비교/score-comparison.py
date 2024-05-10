tmp = input()
arr = tmp.split()
A = int(arr[0])
B = int(arr[1])

tmp1 = input()
arr1 = tmp1.split()
C = int(arr1[0])
D = int(arr1[1])

if A > C and B > D :
    print(1)
else:
    print(0)