def mean(a):
    length=len(a)
    s=sum(a)
    return s/length if length > 0 else 0

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)