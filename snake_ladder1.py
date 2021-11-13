import random as r

dice={}
dice_roll=[1,2,3,4,5,6]
dict_ladder={1:38,4:14,8:10,21:42,28:76,50:67,71:92,88:99}
dict_ladder_keys=list(dict_ladder.keys())
dict_ladder_values=list(dict_ladder.values())

dict_snake={32:10,26:6,48:26,62:18,88:24,95:56,97:78}
dict_snake_keys=list(dict_snake.keys())
dict_snake_values=list(dict_snake.values())

num=int(input("Enter number of players:-"))
x=0
print("Enter the player name:-")
while x<num:
    players=input()
    dice[players]=0
    x+=1
dice_keys=list(dice.keys())
player_index=0
def position():
    i=0
    current_score=dice[dice_keys[player_index]]
    new_score=dice[dice_keys[player_index]]+choice
    if not (new_score>100):
        if (new_score in dict_ladder_keys) or (new_score in dict_snake_keys):
            while i<len(dict_ladder):
                if dict_ladder_keys[i]==new_score:
                    print("You got ladder at",current_score,"....Mover up at",dict_ladder_values[i])
                    dice[dice_keys[player_index]]=dict_ladder_values[i]
                    break
                elif dict_snake_keys[i]==new_score:
                    print("You ate by snake at",current_score,".....Move down at",dict_ladder_values[i])
                    dice[dice_keys[player_index]]=dict_ladder_values[i]
                    break
                i+=1
        else:
            dice[dice_keys[player_index]]=new_score
    else:
        pass

while True:
    flag=0
    print("Score is",dice)
    print("Your Turn",dice_keys[player_index])
    input("Press Enter to roll the dice")
    choice=r.choice(dice_roll)
    print("You Got",choice)
    position()
    if choice==6:
        print("You got Second Chance")
    if dice[dice_keys[player_index]]==100:
        print(dice_keys[player_index],"Win the match")
        del dice[dice_keys[player_index]]
        continue

    player_index+=1
    if player_index > num-1:
        player_index=0
print("ScoreBoard:",dice)
