players=[{"name":"sachin","centuries":12,"half_centuries":32,"wickets":200,"hat_trick":8,"top_score":[110,135,160,140,150]},
        {"name":"ricky","centuries":6,"half_centuries":20,"wickets":150,"hat_trick":4,"top_score":[100,110,140,130,120]},
        {"name":"alastair","centuries":8,"half_centuries":15,"wickets":100,"hat_trick":6,"top_score":[170,120,160,140,180]},
        {"name":"jaqueskallis","centuries":2,"half_centuries":10,"wickets":50,"hat_trick":1,"top_score":[100,130,160,170,90]},
        {"name":"mahi","centuries":15,"half_centuries":25,"wickets":300,"hat_trick":10,"top_score":[180,160,150,170,200]}]

count=0

for player in players:
    if(player['centuries'])>=10:
            count+=1
print( f"no of players more than 10 centuries",count)

# def hat_trick(players):
#     for player in players:
#         if player['hat_trick']>5:
#          num_players=cricket(players)
#     print("Number of players more 10 centuries:",count)

# def hat_trick(players):
for player in players:
    if(player["hat_trick"])>5:
        print("player name:",player["name"],"player hat_trick:",player["hat_trick"])

# player_name=cricket(players)


# def score(players):
    # s=score["top_score"]
top_score=0
for player in players:
    if(player['top_score']>top_score):
        top_score=player['top_score']
    # return(top_score)
    print(top_score)


    