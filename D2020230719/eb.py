consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]
}
def electricity_bill(consumer_data):
    reading=consumer_data["eb_reading"]
    for i in range(0,4):
        difference=reading[i+1]-reading[i]
        print(f"month:{i+1}\nunits_consumed:{difference}")
        if difference<100:
            print(f"no need to pay")
        elif difference>=100 and difference<200:
            print(f"bill amount:",difference*2)
        elif difference>=200 and difference<500:
            print(f"bill amount:",difference*5)
        elif difference>=500 and difference<1000:
            print(f"bill amount:",difference*10)
        elif difference>=1000:
            print(f"bill amount:",difference*14)
electricity_bill(consumer_data)