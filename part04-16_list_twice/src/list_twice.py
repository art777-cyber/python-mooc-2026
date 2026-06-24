list_1=[]
list_2=[]
list=[]
while True:
    entry=int(input("New item: "))
    if entry!=0:
        list_1.append(entry)
        list=list_1.copy()
        list_2=[]
        print(f"The list now: {list_1}")
        while True:
            if len(list)!=0:
                list_2.append(min(list))
                list.remove(min(list))
            else:
                break
        print(f"The list in order: {list_2}")
    else:
        break
print("Bye!")


