# Sets up score variable for the quiz.
score = 0

# Defines the main function of the quiz that will execute all questions.
# There are three questions with an introduction and conclusion.

def main():
    print("Welcome to my Quiz about Aotearoa New Zealand!")
    print("There are three questions for this Quiz and you will have a final score.")
    print("You will gain 1 point if you get the question correct and lose a point if you get it incorrect.")
    print("Your current score: " + str(score))
    input("PRESS ENTER TO START.")

    question1()

    question2()

    question3()

    print("That is the end of the Quiz!")
    print("How did you do?")
    print("Your final score is: " + str(score))
    print("What do you think? Do you think you can do better?")
    print("Do you want to replay?")
    input("PRESS R TO REPLAY. PRESS X TO EXIT.")

def question1():
    print("Question 1: What is the capital of New Zealand?")
    answer = input("Is the answer: A: Auckland B: Wellington or C: Christchurch? ")
    print("This was your answer: " + answer)
    if answer == "B":
        print("Well done! You got it right!")
    if answer == "A" or "C":
        print("Uh oh! That's not right...")

def question2():
    print("Question 2: What is the native bird that people from New Zealand are named after?")
    answer = input("Is the answer: \nA: Tui \nB: Tuatara \nC: Kiwi? ").upper().strip()
    print("This was your answer: " + answer)
    if answer == "C":
        print("Well done! You got it right!")
    else:
        print("Uh oh! That's not right...")

def question3():
    print("Question 3: What is the name of New Zealand's national Rubgy union team?")
    answer = input("Is the answer: \nA: All Blacks \nB: Black Ferns \nC: All Whites? ").upper().strip()
    print("This was your answer: " + answer)
    while answer != True:
        if answer == "A" or "ALL BLACKS":
            print("Well done! You got it right!")
            score += 1
            return
        else:
            print("Uh oh! That's not right...")
            score -= 1
            return

main()
