def spruce(n):
    if n>0:
        print("a spruce!")
        n=(2*n)-1
        a=1
        while n>=a:
            sides=(n-a)//2
            print(" "*sides+"*"*a)
            a+=2
        print(" "*((n-1)//2)+"*")
if __name__ == "__main__":
    spruce(3)