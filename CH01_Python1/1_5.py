ls = [int(e) for e in input("Enter All Bid : ").split()]
ls.sort(reverse=True)
if len(ls) <= 1 :
    print("not enough bidder")
elif ls[0] == ls[1]:
    print("error : have more than one highest bid")
else :
    print(f"winner bid is {ls[0]} need to pay {ls[1]}")