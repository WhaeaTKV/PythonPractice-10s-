
print("Welcome to my Quiz about _!")
input("Are you ready to begin?")

print("Question 1: What is the capital of New Zealand?")
answer = input("Is the answer: A: Auckland B: Wellington or C: Christchurch?")
print("This was your answer: " + answer)
if answer == "A":
    print("Well done! You got it right!")
if answer == "B" or "C":
    print("Uh oh! That's not right...")

print("Question 2: What is the native bird that people from New Zealand are named after?")
answer = input("Is the answer: \nA: Tui \nB: Kiwi \nC: Tuatara?").upper().strip()
print("This was your answer: " + answer)
if answer == "B":
    print("Well done! You got it right!")
else:
    print("Uh oh! That's not right...")

print("Question 3: _?")
answer = input("Is the answer: \nA: _ \nB: _ \nC: _?").upper().strip()
print("This was your answer: " + answer)
while answer != "":
    if answer == "_":
        print("Well done! You got it right!")
    else:
        print("Uh oh! That's not right...")