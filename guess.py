secret_number=int(input("Enter your secret number"))
guess_count=0
total_guesses=3
while guess_count< total_guesses:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("correct guess congrats")
        break
else:
    print("Wrong Guess")