def line(num, text):
    if text == "":
        print("*" * num)
    else:
        first=text[0]
        print(first * num)

def triangle(size):
    num=1
    while num<=size:
        line(num, "#")
        num+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
