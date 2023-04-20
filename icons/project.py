from datetime import datetime

name=input("Enter your name:")

lists='''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/liter
paneer  Rs 110/kg
maggi   Rs 50/Each
boost   Rs 90/Each
colgate Rs 85/Each 
'''
price=0
pricelist=[]
Totalprice=0
Finalprice=0
itemlist=[]
quantitylist=[]
plist=[]

#Rates
items={
'rice':20,
'sugar':30,
'salt':20,
'oil':80,
'paneer':110,
'maggi':50,
'boost':90,
'colgate':85,
}
option=int(input("For list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If You want to buy press 1 or 0 for exit:"))
    if inp1==0:
        break
    if inp1==1:
        item=input("Enter Your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            Totalprice+=price
            itemlist.append(item)
            quantitylist.append(quantity)
            plist.append(price)
            gst=(Totalprice*5)/100
            Finalprice=gst+Totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("you entered Wrong number")
    inp=input("can i bill the items yes or no :")
    if inp=='yes':
        pass
        if Finalprice!=0:
            print(25*"=","MY VILLAGE SUPERMARKET",25*"=")
            print(32*" ","HYDERABAD")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ",'Items',8*" ","Quantity",5*" ",'price')
            for i in range(len(pricelist)):
                print(i,10*' ',itemlist[i],10*' ',quantitylist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ","Total Amount:",'Rs',Totalprice)
            print(50*" ","Gst Amount",'Rs',gst)
            print(50*" ","Final Amount:",'Rs',Finalprice)
            print(75*"-")
            print(25*" ","THANKS FOR VISITING")