def calc(val1,val2,opr):
    if(opr == "*"):
        return val1*val2
    elif(opr == "+"):
        return val1 + val2
    elif(opr == "-"):
        return val1 - val2
    elif(opr == "/"):
        if(val2 == 0):
            return f"You can not divide {val2} by {val1}"
        else:
            return val1/val2
    else:
        return "Invalid values"

print(calc(5,6,"+"))
print(calc(5,6,"-"))
print(calc(5,6,"*"))
print(calc(5,6,"/"))
print(calc(5,0,"/"))

