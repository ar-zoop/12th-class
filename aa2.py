a="hello bello"
c=input("enter the letter in string to find ascii of: ")
try:
    if c in a:
        print ("the ascii for", c,"is",ord(c))
except:
    print ("not in the orginal string")
    continue
