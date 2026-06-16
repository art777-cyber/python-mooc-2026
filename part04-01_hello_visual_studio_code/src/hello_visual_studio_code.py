# This line MUST be here so Python knows what 'editor' is
while True:
    editor = str(input("Editor: "))
    if editor.lower() == "visual studio code":
        break
    elif editor.lower() == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
print("an excellent choice!")