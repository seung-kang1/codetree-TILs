tmp = input()
arr = tmp.split()
h = int(arr[0])
w = int(arr[1])
b = int(10000*w)/(h*h)
if b >= 25:
 #   print(f"{b:.0f}")
    print(int(b))
 
    print("Obesity")
if b < 25:
        print(int(b))