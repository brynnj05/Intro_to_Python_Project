import random


def workout_choice():
    """
    Allows the user to choose the workout from a few options and the target stroke rate

    Inputs:
        None

    Outputs:
        tuple, in order:
            workout (str): 3x20' UT2 Steady State, 4x10' AT/UT1 Intervals, or 6x500m TR.
            target_rate (int): Target strokes per minute for that workout.
        None: Returned after five invalid workout or stroke rate answers.

    Side effects:
        Prints workout options and validation messages; reads terminal input.
    """

    attempts = 0

    print("\n Choose your workout for today's practice!")

    print("1. 3x20' UT2 Steady State")
    print("  Three 20 minute pieces at an easy, sustainable pace.")

    print("2. 4x10' AT/UT1 Intervals")
    print("   Four 10 minute pieces at a moderately hard to hard pace.")

    print("3. 6x500m TR")
    print("   Six 500 meter pieces at a high intensity.")

    workout = input("\n Choose your workout! (1/2/3): ").strip()

    while workout not in ["1", "2", "3"] and attempts < 4:
        attempts += 1
        print("Invalid workout choice. Please choose again.")
        workout = input("Choose your workout! (1/2/3): ").strip()

    if workout not in ["1", "2", "3"]:
        print("You entered an invalid answer 5 times. You lose the game!")
        return None

    if workout == '1':
        workout = "3x20' UT2 Steady State"
        min_rate = 16
        max_rate = 20
    elif workout == '2':
        workout = "4x10' AT/UT1 Intervals"
        min_rate = 20
        max_rate = 26
    else:
        workout = "6x500m TR"
        min_rate = 26
        max_rate = 32

    attempts = 0
    target_rate = 0

    print(f"You chose {workout}! Choose a target stroke rate between {min_rate} and {max_rate}. \n"
          "This is how many strokes your crew takes per minute!")

    while attempts < 5:
        try:
            target_rate = int(input("Target stroke rate: "))

            if min_rate <= target_rate <= max_rate:
                break

        except ValueError:
            pass

        attempts += 1
        if attempts < 5:
            print(f"Invalid stroke rate. Please choose between {min_rate} and {max_rate}.")

    if attempts == 5:
        print("You entered an invalid answer 5 times. You lose the game!")
        return None

    print(f"You chose a target stroke rate of {target_rate}! Make sure to stick to it!")

    return workout, target_rate


def workout_simulation(experience_level, target_rate, workout):
    """
    Simulates how the rowing workout goes

    Inputs:
        experience_level (str): experienced, intermediate, or novice.
        target_rate (int): Target stroke rate in strokes per minute.
        workout (str): 3x20' UT2 Steady State, 4x10' AT/UT1 Intervals, or 6x500m TR.

    Outputs:
        tuple, in order:
            successful_pieces (int): Pieces within 2 spm of the target rate that meet the split.
            pieces (int): Total pieces in the workout: 3, 4, or 6.

    Side effects:
        Prints workout progress and waits for terminal input.
    """

    if workout == "3x20' UT2 Steady State":
        pieces = 3
    elif workout == "4x10' AT/UT1 Intervals":
        pieces = 4
    else:
        pieces = 6

    if experience_level == "experienced":
        variation = 2
    elif experience_level == "intermediate":
        variation = 3
    else:
        variation = 4

    successful_pieces = 0

    print("\n Your crew is ready to begin the workout!")
    print("\n A piece is successful if your actual stroke rate is within 2 strokes")
    print("per minute (spm) of your target AND your boat meets the target split (speed).")

    input("\n Press Enter to start the first piece...")

    for piece in range(pieces):
        actual_rate = target_rate + random.randint(-variation, variation)
        meeting_split = random.choice([True, False])

        print(f"\n Piece {piece + 1}:")
        print(f"Target stroke rate: {target_rate}")
        print(f"Actual stroke rate: {actual_rate}")

        if actual_rate < target_rate:
            print("Coach says: Increase the rate!")
        elif actual_rate > target_rate:
            print("Coach says: Decrease the rate!")
        else:
            print("Coach says: Maintain the rate!")

        input("\n Press Enter to see if your crew is meeting the target split...")

        if meeting_split:
            print("\n Your boat is meeting the target split!")
        else:
            print("\n Your boat is not meeting the target split.")

        input("\n Press Enter to see if your piece was successful...")

        if abs(actual_rate - target_rate) <= 2 and meeting_split:
            successful_pieces += 1
            print("\n Successful piece! You maintained your target rate")
            print("within 2 spm AND met the target split!")

        elif abs(actual_rate - target_rate) > 2 and not meeting_split:
            print("\n Unsuccessful piece! Your stroke rate was more than")
            print("2 spm from the target AND you did not meet the target split.")

        elif abs(actual_rate - target_rate) > 2:
            print("\n Unsuccessful piece! You met the target split,")
            print("but your stroke rate was more than 2 spm from the target.")

        else:
            print("\n Unsuccessful piece! Your stroke rate was within")
            print("2 spm of the target, but you did not meet the target split.")

        if piece < pieces - 1:
            input("\n Take a quick recovery break! Press Enter to start the next piece...")

    print(f"\n Workout complete! You finished {successful_pieces} successful pieces out of {pieces}!")

    return successful_pieces, pieces


def random_event(raining):
    """
    Randomly generates an event during practice based on the weather

    Inputs:
        raining (bool): Whether it is raining.

    Outputs:
        outcome (str): Event result, either positive or negative.

    Side effects:
        Prints the selected random event.
    """

    if raining:
        events = [
            ("Your crew handles the rain really well!", "positive"),
            ("The rain makes it difficult to grip the oar handle!", "negative"),
            ("Someone catches a crab because of the rain!", "negative")
        ]
    else:
        events = [
            ("Your crew has a great power ten!", "positive"),
            ("The water is perfectly flat!", "positive"),
            ("Someone catches a crab!", "negative")
        ]

    event, outcome = random.choice(events)

    print("\n Random event:", event)

    return outcome


def result_calculation(practice_score):
    """
    Determines how successful the rowing practice was.
    Prints a win for scores of at least 8, otherwise a loss.

    Inputs:
        practice_score (int): Total points earned during the game.

    Outputs:
        None

    Side effects:
        Prints the final score and whether the player wins or loses.
    """
    print("Final practice score:", practice_score)

    if practice_score >= 8:
        print("Congratulations! You had a successful rowing practice!")
        print("You win!")
    else:
        print("Your rowing practice could have gone better.")
        print("You lose! Better luck next time!")
