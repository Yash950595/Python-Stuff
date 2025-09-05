player_scores={
    "player_1": 1500,
    "player_2": 2100,
    "player_3": 2900,
    "player_4": 3200,
    "player_5": 5300,
    "player_6": 7000

}

player_league={}

for score,player_league in player_scores:
    score = player_scores[score]

    if score>= 1000:
        player_scores[score]="Bronze League"
        print(player_scores)
    elif score>= 2000:
         player_scores[score]="Silver League"
         print(player_scores)
    elif score >=3000:
         player_scores[score]=" Gold League"
         print(player_scores)
    elif score >= 5000:
         player_scores[score]="Diamond League"
         print(player_scores)
else:
      player_scores[score]="Champion League"
      print(player_scores)