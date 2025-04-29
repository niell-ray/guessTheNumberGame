import random as rand
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number b/w 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

answer = rand.randint(1, 101)
# print(answer)
lives_easy = 10
lives_hard = 5


def compare(lives):
    while lives > 0:
        print(f"You have got {lives} live(s) left.")
        guess = int(input("make a guess? "))

        if guess > answer:
            print("Too high.\n")
            lives -= 1
        elif guess < answer:
            print("Too low.\n")
            lives -= 1
        elif guess == answer:
            print("yes u got the right number, u won!\n")
            break
    if lives == 0:
        print(f"u ran out of lives, u lost, the number was {answer}.")


if difficulty == 'easy':
    compare(lives_easy)

elif difficulty == 'hard':
    compare(lives_hard)
