import random
from collections import Counter


def number_guessing_game():
    print("\n========== NUMBER GUESSING GAME ==========")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("\n🎉 Congratulations!")
                print("You guessed the correct number!")
                print("Number:", secret_number)
                print("Attempts:", attempts)

                score = max(100 - (attempts - 1) * 10, 10)
                print("Score:", score)

                break

        except ValueError:
            print("❌ Please enter a valid number.")


def word_counter():
    print("\n========== WORD COUNTER ==========")

    filename = input("Enter text file name (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().split()
        word_count = len(words)

        # Remove punctuation
        cleaned_words = []

        for word in words:
            word = word.strip(".,!?;:'\"()[]{}")
            if word:
                cleaned_words.append(word)

        frequency = Counter(cleaned_words)

        print("\n---------- RESULT ----------")
        print("Total words:", word_count)

        print("\nWord Frequency:")
        for word, count in frequency.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("❌ File not found!")
        print("Please check the file name and try again.")


def main():
    while True:
        print("\n==========================================")
        print(" NUMBER GUESSING GAME & WORD COUNTER")
        print("==========================================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")
        print("==========================================")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("\nThank you for using the program! 👋")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()