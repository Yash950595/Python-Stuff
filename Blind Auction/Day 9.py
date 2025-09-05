programming_dictonary={
    "Bug": "Error in the code",
    "Loop": "Repeated execution of code",
    "Append": "Adds a new elements at the end of the list"
}
programming_dictonary["input"]="Allows uder to put their own values/content"
print(programming_dictonary)

#wiping a dictionary:
#programming_dictonary={}
#print(programming_dictonary)

#editing the values:
programming_dictonary["Bug"]="Moth in ur computer"
print(programming_dictonary)


player_scores = {
    "player_1": 1500,
    "player_2": 2100,
    "player_3": 2900,
    "player_4": 3200,
    "player_5": 5300,
    "player_6": 7000
}

player_league = {}

# Iterate over the original dictionary
for player, score in player_scores.items():
    if score >= 5000:
        player_league[player] = "Champion League"
    elif score >= 3000:
        player_league[player] = "Diamond League"
    elif score >= 2000:
        player_league[player] = "Gold League"
    elif score >= 1000:
        player_league[player] = "Silver League"
    else:
        player_league[player] = "Bronze League"

# Print the resulting dictionary
print(player_league)
