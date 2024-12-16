import random 
print("Welcome to the Tuple Game!! \n Lets Begin...\n Lets roll to 50!")
#initializing variables
six_sided_die = [1,2,3,4,5,6]
score = 0
round = 1
game_summary = {}
#function imitates rolling dice
def dice_rolling():
    return random.choices(six_sided_die, k = 3)
#function updates round summary for reroll
def re_roll_dictionary (game_summary, round, dice_number, dice_sum, score):
    game_summary[round]["Re-Roll"] = dice_number
    game_summary[round]["Updated Round Total"] = dice_sum
    game_summary[round]["Updated Cumulative Score"] = score
    return game_summary[round] 
#function imitates rolling triples
def triple_roll(dice_number):
 if (dice_number[0] == dice_number[1] == dice_number[2]):
        print("You scored a triple! Game over, Tuple out :(")
        return dice_number
#User plays up to 50 points
while score < 50:
    dice_number = dice_rolling()
    dice_sum = sum(dice_number)
    score += dice_sum
    #dictionary for summary of game at the end 
    game_summary[round] = {
        "Roll": dice_number,
        "Sum of Rolls": dice_sum,
        "Cumulative Score": score
    }
    print(f"Roll: {dice_number}, Score {score}")
    if triple_roll(dice_number):
        break
    # Check if all three values are unique (no doubles)
    if dice_number[0] != dice_number[1] and dice_number[1] != dice_number[2] and dice_number[2] != dice_number[0]:
        re_roll = input("All numbers are unique! Would you like to re-roll (y/n)? ").lower()
        if re_roll == "y":
            score -= dice_sum
            dice_number = dice_rolling()
            dice_sum = sum(dice_number)
            score += dice_sum
            re_roll_dictionary (game_summary, round, dice_number, dice_sum, score)
            print(f"Your new roll is: {dice_number}, and your new score is: {score}")
        else:
            print(f"You kept your roll: {dice_number}. Score remains: {score}")
    else:
        # Find doubles
        double_value = True
        for value in dice_number:
            if dice_number.count(value) == 2:
                double_value = value
                break
        # Keep the double and re-roll the unmatched number
        if double_value:
            re_roll = input("You have a double! Would you like to re-roll the unfixed number (y/n)? ").lower()
            if re_roll == "y":
                old_value = False
                #takes unfixed number and re rolls it
                for i in dice_number:
                    if i != double_value:
                        old_value = i
                        break
                new_dice = []
                new_dice.append(double_value)
                new_dice.append(double_value)
                new_value = random.choice(six_sided_die)
                new_dice.append(new_value)
                dice_number = new_dice
                score -= sum([double_value, double_value, old_value])
                score += sum(new_dice)
                re_roll_dictionary (game_summary, round, dice_number, dice_sum, score)
                print(f"Your new roll is: {dice_number}, and your new score is: {score}")
            #game stops if theres a triple after a double
            if triple_roll(dice_number):
                break
        else:
            print(f"You kept your roll: {dice_number}. Score remains: {score}")
    round += 1
#Output
print(f"Your total score is {score}. Thanks for playing!")
print("Game Summary:")
#updating game summary dictionary for each round
for rnd in game_summary:
    print(
        f"Round {rnd}: Roll = {game_summary[rnd]['Roll']}, "
        f"Sum of Rolls = {game_summary[rnd]['Sum of Rolls']}, "
        f"Cumulative Score = {game_summary[rnd]['Cumulative Score']}"
    )