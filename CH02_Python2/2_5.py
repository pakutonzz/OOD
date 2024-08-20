def bon(w):
    repeat_chars = {}
    for char in w:
        if w.count(char) > 1:
            if char not in repeat_chars:
                repeat_chars[char] = w.count(char)
    
    value = 0
    for char in repeat_chars.keys() :
        value += ord(char)-96

    return value*4
        
word = input("Enter secret code : ")
print(bon(word))