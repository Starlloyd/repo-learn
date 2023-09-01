questions = ("How many wonders of the earth are  there?: ",
                       "I have 30 candies, I eat 28. What do i have now (PLs be wise) ",
                       "When is a door not a door?: ",
                       "The taller i am the younger i am,while the shorter i am the older i am.What am i?: ",
                       "What has to be broken before it can be used?: ",
                       "What month of the year has 28 days?: ",
                       "What has many keys yet opens no luck?: ",
                       "What has teeth but can't bite?: ",
                       "How many types of rocks are there?",
                       "What gets wet while drying?: ")

options = (("A. 5", "B. 7", "C. 10", "D. 12"),
                    ("A. 2", "B. A BURNT TONGUE", "C. SUGAR RUSH", "D. DIABETES"),
                    ("A. JAIL", "B. GATE", "C. A JAR", "D. CONTAINER"),
                    ("A. CANDLE", "B. CONFUSED", "C. A GIRAFFE", "D. A STRAW"),
                    ("A. A GLASS PEN", "B. AN EGG", "C. A MATCH STICK", "D. NONE"),
                    ("A. FEBRUARY", "B. OCTOBER", "C. ALL OF THE MONTHS", "D. NONE OF THEM"),
                    ("A. PASSWORD", "B. PIANO", "C.PIN", "D. KEYHOLDER"),
                    ("A. SHIWAWA", "B. COMB", "C. RABBIT", "D. CHARGER"),
                    ("A. THREE", "B. TWO", "C. SEVEN", "D.Four"),
                    ("A. FAN", "B. TOWEL", "C. CONFIDENCE", "D. SKY")
                    )

answers = ("B", "D", "C", "A", "B", "C", "B", "B", "A", "B") 
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

if score >= 60:
    print("🥇Congratulations🏆")
elif score == 50:
    print("You tried, but next time try harder")
else:
    print("Learn to research") 