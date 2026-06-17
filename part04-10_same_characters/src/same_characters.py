def same_chars(a, b, c):
    if b<len(a) and c<len(a):
        if a[b] == a[c]:
            return True
        else:
            return False
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))