from datetime import datetime 

name=input("Enter name:")

lists='''
Rice     Rs 20/Kg
Sugar    Rs 40/Kg
Salt     Rs 15/Kg
oil      Rs 115/lit
paneer   Rs 100/Kg
Maggi    Rs 50/Kg
Boost    Rs 90/each
Colgate  Rs 70/each
'''
#Declarartion
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates per item
items={'rice':20,'sugar':40,'Salt':15,'oil':115,'paneer':100,'maggi':50,'boost':90,'colgate':70}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
         item=input("enter your items:")
         quantity=int(input("enter quantity:"))
         if item in items.keys():
             price=quantity*(items[item])
             pricelist.append((item,quantity,price))
             totalprice+=price
             ilist.append(item)
             qlist.append(quantity)
             plist.append(price)
             gst=(totalprice*5)/100
             finalamount=gst+totalprice
         else:
             print("The item os not available")
else:
    print("Entered wrong number")
inp=input("can i bill the items yes or no:")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"=","Tharun supermarket",25*"=")
        print(28*" ","Narsipatnam")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
        for i in range(len(pricelist)):
             print(i,4*' ',5*' ',ilist[i],8*' ',qlist[i],10*" ",plist[i])
        print(75*"-")
        print(50*" ",'Toatalamount:','Rs',totalprice)
        print("gst amount",40*" ",'Rs',gst)
        print(75*"-")
        print(50*" ",'finallamount:','Rs',finalamount)
        print(75*"-")
        print(20*" ","Thanks for Visiting")
    
         
    
     