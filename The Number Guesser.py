import random, math

def get_limits():
    while True:
        try:
            lower = int(input("Enter Lower limit: "))
            upper = int(input("Enter Upper limit: "))
            if lower >= upper:
                print("Lower limit must be less than upper limit.")
                continue
            return lower, upper
        except ValueError:
            print("Please enter valid integers.")

def get_feedback(guess):
    while True:
        reply = input(f"Is it {guess}? (h = too high, l = too low, c = correct): ").lower()
        if reply in ['h', 'l', 'c']:
            return reply
        print("Invalid input, enter 'h', 'l', or 'c'.")

def play_game():
    lower, upper = get_limits()
    count = 0
    stopper = round(math.log2(upper - lower + 1))
    print(f"I will guess your number in at most {stopper} tries!")

    guesses = set()
    
    while True:
        if upper - lower < 4:
            guess = random.randint(lower + 1, upper - 1)
        else:
            guess = (upper + lower) // 2
        
        # Avoid repeating guesses
        while guess in guesses:
            guess = random.randint(lower + 1, upper - 1)
        guesses.add(guess)
        count += 1

        feedback = get_feedback(guess)

        if feedback == 'c':
            print(f"I guessed it in {count} tries!")
            if count > stopper:
                print("Hmm, that took longer than expected!")
            break
        elif feedback == 'h':
            upper = guess
        elif feedback == 'l':
            lower = guess

def main():
    print("🎲 Welcome to Number Akinator! 🎲")
    while True:
        start = input("Do you want to play? (yes/no): ").lower()
        if start != 'yes':
            break
        play_game()
    print("Bye!")

main()
