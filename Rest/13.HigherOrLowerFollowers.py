from Data_of_influencers_for_higher_and_lower import data
import random

def influencer():
    influencer = random.choice(data)
    influencer_name = influencer['name']
    influencer_follower_count = influencer['follower_count']
    influencer_description = influencer['description']
    influencer_country = influencer['country']
    # print(f"{influencer_name} a {influencer_description} from {influencer_country}")
    return  influencer_name,influencer_follower_count,influencer_country,influencer_description
game_should_continue= True

while game_should_continue:
    print("Welcome in Higher or lower game, you have to guess which account on instagram has more followers! \nLet's goo! ")
    game_points = 0
    i1 = influencer()
    i2 = influencer()
    print(f"Compare A: {i1[0]} a {i1[3]} from {i1[2]}")
    while i1 == i2:
        i2 = influencer()

    print(f"Compare B: {i2[0]} a {i2[3]} from {i2[2]}")

    while True:
        HorL = input(f"\nWho has more followers? 'A' ({i1[0]}) or 'B'({i2[0]}) ?: ").lower()
        if (i1[1] > i2[1] and  HorL == 'a') or (i1[1] < i2[1] and  HorL == 'b'):
            game_points +=1
            i1 = i2
            print(f"\nNice! You have {game_points} points \n ")
            print(f"Compare A: {i1[0]} a {i1[3]} from {i1[2]}")
            i2 = influencer()

            while i1 == i2:
                    i2 = influencer()

            print(f"Compare B: {i2[0]} a {i2[3]} from {i2[2]}")

        else:

            print(f"\nYou lose...{i1[0]} has {i1[1]} million followers, {i2[0]} has {i2[1]} million followers.\nYou ended with {game_points} points \nGoodbye!")
            #break
            game_should_continue = False