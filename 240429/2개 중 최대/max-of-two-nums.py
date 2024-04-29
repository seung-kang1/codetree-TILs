tmp = input()
arr = tmp.split()
a = int(arr[0])
b = int(arr[1])
c = a if a > b else b
print(c)