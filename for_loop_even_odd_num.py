# even or odd number up to num(50)
list_even=[]
list_odd=[]
for i in range(50):
    if i%2==0:
        list_even.append(i)
    elif i%2!=0:
        list_odd.append(i)
print(list_even)
print(list_odd)
