#Implementing my own split function

def mysplit(strng, delim = " "):
    length = len(strng)
    output = []
    i = 0
    word = ""
    while i < length:
        word += strng[i]
        
        if strng[i] == delim or i == length-1:
            output.append(word)
            word = ""
            
        i = i + 1
    return output
    
print mysplit("my name is harman")
print mysplit("2,3,5,6,7,8,9,3",",")