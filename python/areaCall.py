from areaClass import *

a=Area()
choice=int(input("Enter Your Choice"))
           
if(choice==1):
    r=float(input("Enter Radius"))
    Area.circle(r)
           
elif(choice==2):
    l=float(input("Enter Length"))
    b=float(input("Enter Breadth"))
    Area.rectangle(l,b)

elif(choice==3):
    h=float(input("Enter Height"))
    b=float(input("Enter Base"))
    Area.rectangle(h,b)
    
else: 
    print("wrong input")
    

    
