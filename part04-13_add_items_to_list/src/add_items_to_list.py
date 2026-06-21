num=int(input("How many items: "))
n=1
list=[]
while n<=num:
    entry=int((input("Item " + str(n) + ": ")))
    list.append(entry)
    n+=1
print(list)