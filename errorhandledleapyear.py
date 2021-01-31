
coffee=2
tea=1
while(tea==1):
    while coffee==2:
        val=input("enter a year")
        try:
            mark = int(val)
            coffee=1
        except ValueError:
            print('\nYou did not enter a valid integer')
    val=int(val)       
    if((val%4==0) and (val%100!=0) or (val%400==0)):
        print(val,"is a leap year")
        tea=0
    else:
        print(val,"is not a leap year")
        tea=0
