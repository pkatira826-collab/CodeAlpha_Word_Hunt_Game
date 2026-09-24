import random

# -------------------------------
# WORD HUNT CHALLENGE
# CodeAlpha - Python Internship
# -------------------------------

word_bank = {
    "easy": [
        ("apple", "A fruit"),
        ("tiger", "A wild animal"),
        ("pizza", "A popular Italian food"),
        ("music", "You listen to it"),
        ("river", "Water flowing naturally")
    ],

    "medium": [
        ("python", "A programming language"),
        ("laptop", "A portable computer"),
        ("college", "A place where students study"),
        ("internet", "Used to connect computers"),
        ("developer", "A person who creates software")
    ]
}

MAX_WRONG = 6


def show_hangman(wrong):
    stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,

        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]

    print(stages[wrong])


def choose_word():
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")

    while True:
        choice = input("Enter choice: ").strip()

        if choice == "1":
            return random.choice(word_bank["easy"])

        elif choice == "2":
            return random.choice(word_bank["medium"])

        else:
            print("Please choose 1 or 2.")


def play_game():

    word, hint = choose_word()

    guessed = set()
    wrong_guesses = 0
    score = 100

    print("\n" + "=" * 45)
    print("       🎯 WORD HUNT CHALLENGE")
    print("=" * 45)

    print(f"\nHint: {hint}")

    while wrong_guesses < MAX_WRONG:

        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Score:", score)
        print("Wrong guesses:", wrong_guesses, "/", MAX_WRONG)

        if all(letter in guessed for letter in word):
            print("\n🎉 YOU WON!")
            print("The word was:", word)
            print("Final Score:", score)
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter exactly one alphabet.")
            continue

        if guess in guessed:
            print("⚠️ You already tried that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Correct!")
            score += 10
        else:
            print("❌ Wrong!")
            wrong_guesses += 1
            score -= 15

        show_hangman(wrong_guesses)

    print("\n💀 GAME OVER!")
    print("The correct word was:", word)
    print("Final Score:", max(score, 0))


# -------------------------------
# MAIN PROGRAM
# -------------------------------

while True:

    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing Word Hunt! 👋")
        break