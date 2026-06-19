list=[1, 2, 3, 4, 5]
index=0
while True:
    index=int(input("Index: "))
    if index!=-1:
       newvalue=int(input("New value: "))
       list[index]=newvalue
       print(list)
    else:
      break