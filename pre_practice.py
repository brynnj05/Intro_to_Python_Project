import random


def generate_weather():
    """
    Randomly generates the weather for rowing practice

    Inputs:
        None

    Outputs:
        tuple, in order:
            temperature (int): Outdoor temperature in degrees Fahrenheit.
            weather (str): Weather condition, either sunny or cloudy.
            raining (bool): Whether it is raining.

    Side effects:
        Prints the generated weather.
    """

    temperature = random.randint(25, 80)
    weather = random.choice(["sunny", "cloudy"])
    raining = random.choice([True, False])

    print("It is", temperature, "degrees and", weather, "outside.")

    if raining:
        print("It is also raining!")
    else:
        print("It is not raining.")

    return temperature, weather, raining


def clothing_choice(temperature, weather, raining):
    """
    Determines what clothes the user should wear based on the temperature and weather

    Inputs:
        temperature (int): Outdoor temperature in degrees Fahrenheit.
        weather (str): Weather condition, either sunny or cloudy.
        raining (bool): Whether it is raining.

    Outputs:
        tuple, in order:
            shirt (str): long sleeve, short sleeve, or tank top.
            outer_layer (str): jacket, half-zip, raincoat, or none.

    Side effects:
        Prints the clothing recommendation.
    """

    if temperature <= 45:
        shirt = "long sleeve"
        outer_layer = "jacket"
    elif temperature <= 65:
        shirt = "short sleeve"
        outer_layer = "half-zip"
    else:
        shirt = "tank top"
        outer_layer = "none"

    if raining:
        outer_layer = "raincoat"

    if outer_layer == "none":
        print("You should wear a", shirt)
    else:
        print("You should wear a", shirt, "and a", outer_layer)

    return shirt, outer_layer


def snack_choice():
    """
    Allows the user to choose a pre-workout snack

    Inputs:
        None

    Outputs:
        snack (str): banana, granola bar, or none.
        None: Returned after five invalid answers.

    Side effects:
        Prompts for terminal input and prints validation messages.
    """

    attempts = 0

    snack = input("Choose a pre-workout snack (banana/ granola bar/ none): ").strip().lower()

    while snack not in ["banana", "granola bar", "none"] and attempts < 4:
        attempts += 1
        print("Invalid snack choice. Please choose again.")
        snack = input("Choose a pre-workout snack! (banana/granola bar/none): ").strip().lower()

    if snack not in ["banana", "granola bar", "none"]:
        print("You entered an invalid answer 5 times. You lose the game!")
        return None

    return snack


def boat_choice():
    """
    Allows the user to choose which type of boat they want to row

    Inputs:
        None

    Outputs:
        boat (str): eight, four, or pair.
        None: Returned after five invalid answers.

    Side effects:
        Prompts for terminal input and prints validation and choice messages.
    """
    attempts = 0

    boat = input("Choose which boat you would like to row in! (eight/four/pair): ").strip().lower()

    while boat not in ["eight", "four", "pair"] and attempts < 4:
        attempts += 1
        print("Invalid boat choice. Please choose again.")
        boat = input("Choose which boat you would like to row in! (eight/four/pair): ").strip().lower()

    if boat not in ["eight", "four", "pair"]:
        print("You entered an invalid answer 5 times. You lose the game!")
        return None

    print("You chose to row in the", boat)

    return boat


def seat_assignment(boat):
    """
    Randomly assigns the user a seat based on the chosen boat

    Inputs:
        boat (str): Selected boat: eight, four, or pair.

    Outputs:
        seat (int): Seat number, from 1 to the number of rowers.

    Side effects:
        Prints the seat assignment and its role.
    """

    if boat == "eight":
        seat = random.randint(1, 8)

        print("You were assigned seat", seat, "in the eight!")

        if seat == 1 or seat == 2:
            print("You're in the bow pair! Your job is to help with balance and technique.")
        elif seat >= 3 and seat <= 6:
            print("You're in the engine room! Your job is to provide power.")
        elif seat == 7:
            print("You're right behind stroke seat! You help maintain the rhythm.")
        else:
            print("You're in stroke seat! You set the rhythm for the crew.")

    elif boat == "four":
        seat = random.randint(1, 4)

        print("You were assigned seat", seat, "in the four!")

        if seat == 1:
            print("You're in bow seat! Your job is to help with balance and technique.")
        elif seat == 4:
            print("You're in stroke seat! You set the rhythm for the crew.")
        else:
            print("You're in the middle pair! Your job is to provide power and maintain rhythm.")

    else:
        seat = random.randint(1, 2)

        print("You were assigned seat", seat, "in the pair!")

        if seat == 1:
            print("You're in bow seat! Your job is to help with balance and steering.")
        else:
            print("You're in stroke seat! You set the rhythm for the pair.")

    return seat


def crew_experience():
    """
    Randomly determines the rowing experience of the crew

    Inputs:
        None

    Outputs:
        experience_level (str): experienced, intermediate, or novice.

    Side effects:
        Prints the generated experience level.
    """

    experience_level = random.choice(["experienced", "intermediate", "novice"])

    print("Your crew's experience level is:", experience_level)

    return experience_level


def reaction(situation):
    """
    Allows the user to react to different situations during practice

    Inputs:
        situation (str): Situation the user is reacting to.

    Outputs:
        reaction (str): excited, indifferent, or frustrated.
        None: Returned after five invalid answers.

    Side effects:
        Prompts for terminal input and prints validation messages.
    """

    attempts = 0

    print(f"\n How do you feel about {situation}?")

    reaction = input("Choose your reaction! (excited/indifferent/frustrated): ").strip().lower()

    while reaction not in ["excited", "indifferent", "frustrated"] and attempts < 4:
        attempts += 1
        print("Invalid reaction! Please try again.")
        reaction = input("Choose your reaction! (excited/indifferent/frustrated): ").strip().lower()

    if reaction not in ["excited", "indifferent", "frustrated"]:
        print("You entered an invalid answer 5 times. You lose the game!")
        return None

    return reaction
