players=[{"name":"sachin","centuries":12,"half_centuries":32,"wickets":200,"hat_trick":8,"top_score":150},
        {"name":"ricky","centuries":6,"half_centuries":20,"wickets":150,"hat_trick":4,"top_score":120},
        {"name":"alastair","centuries":8,"half_centuries":15,"wickets":100,"hat_trick":6,"top_score":180},
        {"name":"jaqueskallis","centuries":2,"half_centuries":10,"wickets":50,"hat_trick":1,"top_score":90},
        {"name":"mahi","centuries":15,"half_centuries":25,"wickets":300,"hat_trick":10,"top_score":200}]
def century(players):
    for player in players:
        if player["centuries"]>10:
            # name=players["name"]
            # centuries=players["centuries"]
            print("player name:",player["name"],"player centuries:",player["centuries"])
century(players)


def hat_trick(players):
    for player in players:
        if player["hat_trick"]>5:
            print("player name:",player["name"],"player hat_trick:",player["hat_trick"])
hat_trick(players)


def score(players):
    top_score=0
    for player in players:
        if player['top_score']>top_score:
            top_score=player['top_score']
    return(top_score)
            # print("player name:",player["name"],"player top_score:",(players(top_score)))
print(score(players))
    # return score(players)
# score(players)

    