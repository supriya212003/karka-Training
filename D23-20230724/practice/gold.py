month_gold_rate=[{
    "month":"january",
    "gold_rate":1500},
    {
    "month":"february",
    "gold_rate":2000},
    {
    "month":"march",
    "gold_rate":1000}]


min=month_gold_rate[0]["gold_rate"]
for rate in month_gold_rate:
    rates=rate['gold_rate']
    month=rate["month"]
    if min>=rates:
        min=rates
        mon=month
print(min)
print(f"{mon}:{min}")
# rate=0

# if month_gold_rate[0]["gold_rate"]<month_gold_rate[1]["gold_rate"]:
#     if month_gold_rate[0]["gold_rate"]<month_gold_rate[2]["gold_rate"]:
#         print(month_gold_rate[2])
# if month_gold_rate[1]["gold_rate"]<month_gold_rate[2]["gold_rate"]:
#     print(month_gold_rate[1])
# else:
#     print(month_gold_rate[2])
    


     
        

    
