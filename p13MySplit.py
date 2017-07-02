#Implementing my own split function

def mysplit(strng, delim = " "):
    length = len(strng)
    output = []
    i = 0
    word = ""
    while i < length:
        if strng[i] != delim or i == length - 1:
            word += strng[i]
            if i == length - 1:
                output.append(word)
        else:
            output.append(word)
            word = ""
            
        i = i + 1
    return output
    
#print mysplit("my name is harman")
#print mysplit("2,3,5,6,7,8,9,3",",")

#using For
def mysplit2(sentence, delim = " "):
    output = []
    word = ""
    #use enumerate for using index of a list/sequence
    for idx, letter in enumerate(sentence):
        if letter != delim or idx == len(sentence) - 1:
            word += letter
        else:
            output.append(word)
            word = ""
    else:
        output.append(word) # else block of FOR loop runs if no break occurs, Here else: 
                            # was not required, it's just for demonstration
    return output
            
#print mysplit2("The universe is unfathomable")
#print mysplit2("2,3,5,6,7,8,9,3",",")
        