def line(num, text):
    if text == "":
        print("*" * num)
    else:
        first=text[0]
        print(first * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")