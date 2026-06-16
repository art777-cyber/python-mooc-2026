def line(num, text):
    if text == "":
        print("*" * num)
    else:
        first=text[0]
        print(first * num)
def triangle(width  , character1):
    num=1
    while num<=width:
        line(num, character1)
        num+=1
def rect(width, height, character2):
    while height>0:
        line(width,character2)
        height-=1
def shape(width, character1, height, character2):
    triangle(width, character1)
    rect(width, height, character2)  

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")