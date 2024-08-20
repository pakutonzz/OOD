print("*** Reading E-Book ***")
text, hl = map(str,input("Text , Highlight : ").split(","))

i = 0

while i < len(text):
    if text[i:i+len(hl)] == hl:
        print(f"[{hl}]", end='')
        i += len(hl)
    else:
        print(text[i], end='')
        i += 1