def bhalluk(n:int)-> int:
    if n==0 or n==1:
        return 1
    return n*bhalluk(n-1)
print(bhalluk(5))