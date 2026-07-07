import random

# Choices
choices = ["rock", "paper", "scissors"]

print("=" * 35)
print("🎮 Rock Paper Scissors Game")
print("=" * 35)

while True:
    user = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose      : {user.capitalize()}")
    print(f"Computer chose : {computer.capitalize()}")

    if user == computer:
        print("🤝 It's a Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        break