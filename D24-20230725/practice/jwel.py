month_gold_rate=[{
    "month":"january",
    "gold_rate":1500,
    "jwel_list":[{
        "name":"chain",
        "making_cost":10
    },
    {
        "name":"ring",
        "making_cost":14
    }]},
    {
    "month":"february",
    "gold_rate":2000,
    "jwel_list":[{
        "name":"chain",
        "making_cost":10
    },
    {
        "name":"ring",
        "making_cost":14
    }]},
    {
    "month":"march",
    "gold_rate":1000,
    "jwel_list":[{
        "name":"chain",
        "making_cost":10
    },
    {
        "name":"ring",
        "making_cost":14
    }]}]
# print(month_gold_rate[0]["jwel_list"][0]["making_cost"])
# print(month_gold_rate[0]["jwel_list"][0])

for i in month_gold_rate:
    mon=i["month"]
    rate=i['gold_rate']
    print(mon)
    print(rate)
    for j in i["jwel_list"]:
        cost=j["making_cost"]
        tot=(i["gold_rate"] *cost )/100
        amount=i["gold_rate"]+tot
        jwel=j["name"]
        print(jwel,amount)
        



