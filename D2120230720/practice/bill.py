consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]
}

def electricity_bill(consumer_data):
    reading=consumer_data["eb_reading"]
    list1=[]
    tot=0
    for i in range(1,len(reading)):
        rs=0
        list_details={
            "month":0,
            "units_consumed":0,
            "bill_amount":0
        }
        difference=reading[i]-reading[i-1]
        if difference<100:
            print("no need to pay")
        elif difference>=100 and difference<200:
            rs = difference*2
        
        elif difference>=200 and difference<500:
            rs=difference*5
            
        elif difference>=500 and difference<1000:
            rs=difference*10
            
        elif difference>=1000:
            rs=difference*14
            
            

        list_details={"month":i,"units_consumed":difference,"bill_amount":rs}
        
        
        list1.append(list_details)
    print(list1)
    string=str(list1)
    print(type(string))    
electricity_bill(consumer_data)

