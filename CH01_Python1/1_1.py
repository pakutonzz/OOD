print("*** Converting hh.mm.ss to seconds ***")
h, m, s = map(int, input("Enter hh mm ss : ").split())
result = h*60*60 + m*60 + s
if h>=60 or h<0 :
    print(f"hh({h}) is invalid!")
elif m>=60 or m<0:
    print(f"mm({m}) is invalid!")
elif s>=60 or s<0 :
    print(f"ss({s}) is invalid!")
else :
    print(f"{h:02}:{m:02}:{s:02} = {result:,} seconds")