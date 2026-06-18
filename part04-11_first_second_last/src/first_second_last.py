def first_word(sentence):
    index=sentence.find(" ")
    indexarray=[]
    while index>0:
        indexarray.append(index)
        index=sentence.find(" ",index+1)
    return(sentence[0:indexarray[0]])

def second_word(sentence):
    index=sentence.find(" ")
    indexarray=[]
    while index>0:
        indexarray.append(index)
        index=sentence.find(" ",index+1)
    if len(indexarray)<2:
        return(sentence[indexarray[0]+1:])
    else:
        return(sentence[indexarray[0]+1:indexarray[1]])

def last_word(sentence):
    index=sentence.find(" ")
    indexarray=[]
    while index>0:
        indexarray.append(index)
        index=sentence.find(" ",index+1)
    return(sentence[indexarray[-1]+1:])
    




if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))