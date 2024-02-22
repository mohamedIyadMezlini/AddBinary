def BinToDec(x):
    dec=0
    for i in range(len(x)-1,-1,-1):
        if (x[i] != "0"):
            dec += (pow(2,len(x)-1-i))
    return dec


A,B = input().split()
c=BinToDec(A)
d=BinToDec(B)
s=c+d
print(bin(s)[2:])