tmp = input()
arr = tmp.split()
a = int(arr[0])
b = int(arr[1])
if a > b:
    print(a-b)
if b > a:
    print(b-a)
if a == b:
    print(a-b)