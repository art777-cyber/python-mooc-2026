def line(num, text):
    if text == "":
        print("*" * num)
    else:
        first=text[0]
        print(first * num)

def square_of_hashes(size):
    width=size
    while size>0:
        line(width, "#")
        size-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
