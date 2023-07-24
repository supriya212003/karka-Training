consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]
}
import json
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
        # return list1
        
a=electricity_bill(consumer_data)
print(a)
# string=str(list1)
# print(type(string))    
#bill=electricity_bill(consumer_data)
#list2=str(bill)
#print (list2)
file=open("/home/supriya/karka/D22-20230722/practice/dict.txt","w")
file.write(str(a))
file.close()

save=input("How to save?")
a=save.lower()
if a=="dict":
    file=open("/home/supriya/karka/D22-20230722/practice/dict.txt","w")
    file.write(a)
    file.close()
elif a=="json":
    file=open("/home/supriya/karka/D22-20230722/practice/dict.txt","w")
    file.write(json.dumps(a))
    print((json.dumps(a)))
    file.close()
