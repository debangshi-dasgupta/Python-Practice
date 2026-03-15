

def bear(n:int)-> int:
 d = 1
 for i in range(2,n+1):
     d = d * i
     return d
 print (bear())