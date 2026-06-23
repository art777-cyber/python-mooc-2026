list=[]
while True:
    entry=str(input("Word: "))
    if entry in list:
        break
    else:
        list.append(entry)
print(f"You typed in {len(list)} different words")
