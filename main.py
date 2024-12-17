
import random



def scramble(word):

    char_list = list(word)

    random.shuffle(char_list)

    scrambled = ''.join(char_list)

    return scrambled



easy_words = [

    "apple", "ball", "cat", "dog", "fish", "hat", "ice", "jump", "kite", "moon", "nest", "queen", "red", "sun", "toy", "up", "van", "water",

    "yellow", "zoo", "bed", "cup", "duck", "egg", "fire", "green", "house",

    "king", "lion", "mask", "pen", "sock", "tap", "unit", "vase",

    "wind", "x-ray", "yarn", "zip", "car", "desk", "ear", "golf", "jam",

    "kit", "lip", "mop", "pie", "sit", "toe", "yard", "zero", 

    "bark", "card", "fast", "girl", "hand", "leaf", "nut", "open", "pink",

    "rain", "tail", "worm", "able", "bear", "cake", 

    "doll", "good"

]



medium_words = [

    "archive", "balloon", "castle", "delight", "echo", "forest", "gate", "hero", "island", "jungle",

    "knot", "lantern", "marble", "night", "optic", "paper", "quiver", "rush", "stone", "tent",

    "unique", "vault", "whisper", "zipper", "blue", "calm", "drove", "elevate", "flicker", "grin",

    "honey", "icon", "jelly", "keen", "leap", "maze", "neat", "prism", "quench", "snow", "tail", "veil", "wisp", "zany", "calm", "deer", "echo", "fire",

    "grip", "hold", "iron", "jump", "leaf", "mist", "nest", "oak", "path", "queen",

    "rise", "snap", "track", "unit", "vibe", "wind", "yellow", "zip", "arrow", "bench",

    "cool", "dark", "elk", "front", "green", "hill", "joy", "knotty", "lamp",

    "mint", "nudge", "open", "pouch", "quilt", "ridge", "sand", "vast", "water",

    "yard", "zero", "apple", "boat", "car", "duck", "easy", "fire", "gold", "hope"

]



hard_words = [

    "abandon", "absence", "accomplish", "adventure", "alarming", "amazing", "ancestor", "apparent", "appraise", "arrival",

    "baseball", "backyard", "balance", "barrier", "benefit", "bravery", "calendar", "captain", "century", "chocolate",

    "classic", "collapse", "complete", "condition", "confuse", "control", "courage", "curtain", "dangerous", "decision",

    "develop", "disease", "elastic", "elevate", "exciting", "explorer", "freedom", "general", "hospital", "imagine",

    "journey", "justice", "learning", "library", "magic", "meeting", "memory", "modern", "mountain", "natural",

    "occupy", "original", "passion", "pattern", "permanent", "person", "popular", "progress", "quality", "realistic",

    "reform", "remote", "rescue", "return", "success", "student", "surprise", "tolerate", "travel", "teacher",

    "universe", "vacation", "vehicle", "venture", "version", "victory", "vivid", "welcome", "western", "wildlife",

    "wonderful", "writing", "balanced", "building", "capture", "delivery", "discover", "excited", "family", "financial",

    "happening", "library", "masterpiece", "overcome", "parallel", "priority", "running", "stomach", "tension", "weather"

]



#Intro Screen

print("Welcome to Word Scramble!", end = "")

while True:

    user_difficulty = input(""" 

Choose your difficulty:

Type 1 and Enter for Easy

Type 2 and Enter for Medium

Type 3 and Enter for Hard

Or Type Help and Enter for Instructions

""")

    

    if user_difficulty.lower() == "help":

        print("""

        Word Scramble Game Instructions:

        1. You will be given a scrambled word.

        2. Your task is to guess the original word.

        3. You have 5 attempts to guess the word correctly.

        4. Each incorrect guess will reduce the points you earn for that round.

        5. The game continues for 10 rounds.

        6. Points are awarded based on how quickly you guess the word.

        7. You can choose between Easy, Medium, or Hard difficulty.

        

        Good luck and have fun! :)""")

        continue

    elif user_difficulty in ["1", "2", "3"]:

        break

    else:

        print("Invalid input. Please choose a valid option.")



# Word Scramble Game

round = 1

total_points = 0

if user_difficulty == "1":

    while round < 11:

        print(f"Round {round}")

        number_guesses = 0

        round_points = 10

        random_word = random.choice(easy_words)

        scrambled_word = scramble(random_word)

        while number_guesses < 5:

            user_guess = input(f"Scrambled word: {scrambled_word} \nGuess: ")

            if user_guess != random_word:

                if number_guesses == 4:

                    print("You failed to guess the word. 0 points earned this round.")

                    number_guesses += 1

                else:

                    number_guesses += 1

                    round_points -= 2

                    print(f"Incorrect! Try Again. {5 - number_guesses} guesses remaining.")

            elif user_guess == random_word:

                print(f"You earned {round_points} points this round!")

                total_points += round_points

                break

        round += 1

    print(f"You earned {total_points} total points! Game over.")



if user_difficulty == "2":

    while round < 11:

        print(f"Round {round}")

        number_guesses = 0

        round_points = 10

        random_word = random.choice(medium_words)

        scrambled_word = scramble(random_word)

        while number_guesses < 5:

            user_guess = input(f"Scrambled word: {scrambled_word} \nGuess: ")

            if user_guess != random_word:

                if number_guesses == 4:

                    print("You failed to guess the word. 0 points earned this round.")

                    number_guesses += 1

                else:

                    number_guesses += 1

                    round_points -= 2

                    print(f"Incorrect! Try Again. {5 - number_guesses} guesses remaining.")

            elif user_guess == random_word:

                print(f"You earned {round_points} points this round!")

                total_points += round_points

                break

        round += 1

    print(f"You earned {total_points} total points! Game over.")



if user_difficulty == "3":

    while round < 11:

        print(f"Round {round}")

        number_guesses = 0

        round_points = 10

        random_word = random.choice(hard_words)

        scrambled_word = scramble(random_word)

        while number_guesses < 5:

            user_guess = input(f"Scrambled word: {scrambled_word} \nGuess: ")

            if user_guess != random_word:

                if number_guesses == 4:

                    print("You failed to guess the word. 0 points earned this round.")

                    number_guesses += 1

                else:

                    number_guesses += 1

                    round_points -= 2

                    print(f"Incorrect! Try Again. {5 - number_guesses} guesses remaining.")

            elif user_guess == random_word:

                print(f"You earned {round_points} points this round!")

                total_points += round_points

                break

        round += 1

    print(f"You earned {total_points} total points! Game over.")
