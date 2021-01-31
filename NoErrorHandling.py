tea=1
while(tea==1):
    val=int(input("enter a year"))
    if((val%4==0) and (val%100!=0) or (val%400==0)):
        print(val,"is a leap year")
        tea=0
    else:
        print(val,"is not a leap year")
        tea=0
    
