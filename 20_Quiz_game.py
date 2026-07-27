# Quizz

questions = ["How many elements are there in the periodic table?:",
             "Which animal lays the largest eggs?:",
             "How many bones are there in the human body?:",
             "Which planet is the hottest?:"]

options = [("A.116 ", "B.117 ", "C.118 ", "D.119 "),
           ("A.Ostrich  ", "B.Elephant  ", "C.Crocodile0  ", "D.Whale  "),
           ("A.106  ", "B.206  ", "C.306 ", "D.150  "),
           ("A.Mars ", "B.Mercury  ", "C.Earth  ", "D.Moon  ")]

answers = ("C","A","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    
    
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is correct")
    
    question_num += 1