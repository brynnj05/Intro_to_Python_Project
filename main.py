import pre_practice
import during_practice


def main():
    """
    Run one interactive morning rowing practice.

    Inputs:
        None

    Outputs:
        None

    Side effects:
        Reads terminal input and prints gameplay, scores, and results.
        Calls quit() to terminate the process after maximum attempts.
    """

    # initializing practice score
    practice_score = 0

    # welcoming user to the game
    print("\n Good morning! You've just woken up and have to start getting ready for your rowing practice!")

    # setting the weather
    input("\n Press Enter to see what the weather is like today...")
    temperature, weather, raining = pre_practice.generate_weather()

    # user reacts to weather
    weather_reaction = pre_practice.reaction("the weather")

    if weather_reaction is None:
        quit()

    # practice score updates based on user reaction
    if weather_reaction == "excited":
        practice_score += 2
        print("\n You're excited for practice! You earned 2 points!")
    elif weather_reaction == "indifferent":
        practice_score += 1
        print("\n You're ready to make the most of practice! You earned 1 point!")
    else:
        practice_score -= 1
        print("\n Your frustration affects your mindset! You lost 1 point!")

    print("Current practice score:", practice_score)

    # determining practice clothing
    input("\n Press Enter to see what you should wear to practice...")
    shirt, outer_layer = pre_practice.clothing_choice(temperature, weather, raining)

    # user chooses shirt color
    attempts = 0

    shirt_color = input("\n Choose your shirt color! (green/red/blue): ").strip().lower()

    while shirt_color not in ["green", "red", "blue"] and attempts < 4:
        attempts += 1
        print("Invalid color. Please choose again.")
        shirt_color = input("Choose your shirt color! (green/red/blue): ").strip().lower()

    if shirt_color not in ["green", "red", "blue"]:
        print("You entered an invalid answer 5 times. You lose the game!")
        quit()

    # updating practice score based on shirt color
    if shirt_color == "green":
        practice_score += 2
        print("\n Lighter colors earn more points! You earned 2 points!")
    elif shirt_color == "red":
        practice_score += 1
        print("\n Medium-colored shirts earn some points! You earned 1 point!")
    else:
        print("\n Darker colors earn fewer points. You earned 0 points!")

    print("Current practice score:", practice_score)

    # user chooses outer layer color
    if outer_layer != "none":

        attempts = 0

        outer_color = input("\n Choose your outer layer color! (gray/navy/black): ").strip().lower()

        while outer_color not in ["gray", "navy", "black"] and attempts < 4:
            attempts += 1
            print("Invalid color! Please choose again.")
            outer_color = input("Choose your outer layer color! (gray/navy/black): ").strip().lower()

        if outer_color not in ["gray", "navy", "black"]:
            print("You entered an invalid answer 5 times. You lose the game!")
            quit()

        # updating practice score based on outer layer color
        if outer_color == "gray":
            practice_score += 2
            print("\n Lighter colors earn more points! You earned 2 points!")
        elif outer_color == "navy":
            practice_score += 1
            print("\n Medium-colored outer layers earn some points! You earned 1 point!")
        else:
            print("\n Darker colors earn fewer points. You earned 0 points!")

        print("Current practice score:", practice_score)

    # user chooses their snack
    input("\n Press Enter to choose your pre-workout snack...")
    snack = pre_practice.snack_choice()

    if snack is None:
        quit()

    # practice score updates based on snack choice
    if snack == "none":
        practice_score -= 1
        print("\n You skipped your snack! You lost 1 point!")
    else:
        practice_score += 2
        print("\n You're fueled for practice! You earned 2 points!")

    print("Current practice score:", practice_score)

    # user chooses what boat they want to row in
    input("\n You're ready to head to the boathouse! Press Enter to choose your boat...")
    boat = pre_practice.boat_choice()

    if boat is None:
        quit()

    # user finds out their seat assignment
    input("\n Press Enter to find out your seat assignment...")
    seat = pre_practice.seat_assignment(boat)

    # user reacts to their seat assignment
    seat_reaction = pre_practice.reaction("your assigned seat")

    if seat_reaction is None:
        quit()

    # practice score updates based on user's reaction to seat assignment
    if seat_reaction == "excited":
        practice_score += 2
        print("\n Your positive attitude helps the crew! You earned 2 points!")
    elif seat_reaction == "indifferent":
        practice_score += 1
        print("\n You're ready to make the most of practice! You earned 1 point!")
    else:
        practice_score -= 1
        print("\n Your frustration affects your mindset! You lost 1 point!")

    print("Current practice score:", practice_score)

    # user finds out experience level of their crew
    input("\n Press Enter to find out your crew's experience level...")
    experience_level = pre_practice.crew_experience()

    # user reacts to experience level of their crew
    crew_reaction = pre_practice.reaction("your crew's experience level")

    if crew_reaction is None:
        quit()

    # practice score updates based on user's reaction to crew experience level
    if crew_reaction == "excited":
        practice_score += 2
        print("\n Your positive attitude helps the crew! You earned 2 points!")
    elif crew_reaction == "indifferent":
        practice_score += 1
        print("\n You're ready to work with your crew! You earned 1 point!")
    else:
        practice_score -= 1
        print("\n Your frustration affects your teamwork! You lost 1 point!")

    print("Current practice score:", practice_score)

    # user chooses their workout
    input("\n Press Enter to choose today's workout...")
    workout_result = during_practice.workout_choice()

    if workout_result is None:
        quit()

    workout, target_rate = workout_result

    successful_pieces, pieces = during_practice.workout_simulation(experience_level, target_rate, workout)

    input("\n Press Enter to see if your workout was successful overall...")

    # practice score updates based on workout success
    if successful_pieces / pieces >= 0.65:
        practice_score += 4
        print("\n Great workout! You earned 4 points!")
    elif successful_pieces / pieces >= 0.45:
        practice_score += 2
        print("\n Good effort! You earned 2 points!")
    else:
        practice_score -= 1
        print("\n Your crew struggled during the workout! You lost 1 point.")

    print("Current practice score:", practice_score)

    # random event generated
    input("\n Press Enter to see if anything unexpected happened during practice...")
    outcome = during_practice.random_event(raining)

    # practice score updates based on random event
    if outcome == "positive":
        practice_score += 2
        print("You earned 2 points!")
    else:
        practice_score -= 2
        print("You lost 2 points!")

    print("Current practice score:", practice_score)

    # user is told if they win or lose the game
    input("\n Practice is over! Press Enter to see your final result...")
    during_practice.result_calculation(practice_score)


if __name__ == "__main__":
    main()
