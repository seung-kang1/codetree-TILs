tmp1 = input()
arr1 = tmp1.split()
a = int(arr1[0])
b = arr1[1]

tmp2 = input()
arr2 = tmp2.split()
c = int(arr2[0])
d = arr2[1]

if (a >= 19 or c >=19) and b == "M" or d == "M":
    print("1")
else :
    print("0")