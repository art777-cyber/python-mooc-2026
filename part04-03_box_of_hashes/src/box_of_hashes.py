def line(num, text):
    if text == "":
        print("*" * num)
    else:
        first=text[0]
        print(first * num)

def box_of_hashes(height):
    while height>0:
        line(10, "#")
        height-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
