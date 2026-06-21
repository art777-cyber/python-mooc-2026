list=[]
print("The list is now []")
while True:
    action=str(input("a(d)d, (r)emove or e(x)it: "))
    if action=="d":
        list.append(len(list) + 1)
        print(f"The list is now {list}")
    elif action=="r":
        if len(list)>0:
            list.pop(len(list)-1)
        print(f"The list is now {list}")    
    elif action=="x":
        break
print("Bye!")