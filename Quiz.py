import random

# Questions for different categories with correct answers
math_questions = [
    ("What is the result of 2 + 2?", "4"),
    ("Solve: 5 * 6", "30"),
    ("What is the square root of 64?", "8"),
    ("Calculate: 9 / 3", "3"),
    ("What is the value of 3 squared?", "9"),
    ("What is the perimeter of a square with side length 5?", "20"),
    ("Simplify: 2^3", "8"),
    ("If a = 5 and b = 7, what is the value of a + b?", "12"),
    ("Find x if 3x - 7 = 14", "7"),
    ("What is the area of a circle with radius 4?", "50.24")
]

science_questions = [
    ("What is the chemical symbol for water?", "H2O"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who developed the theory of relativity?", "Albert Einstein"),
    ("What is the largest bone in the human body?", "Femur"),
    ("What causes the tides on Earth?", "Gravitational pull of the moon"),
    ("What is the unit of measurement for force?", "Newton"),
    ("What is the process by which plants make their food?", "Photosynthesis"),
    ("Which gas do plants absorb during photosynthesis?", "Carbon dioxide"),
    ("What is the speed of light in a vacuum?", "299,792 kilometers per second"),
    ("Who discovered penicillin?", "Alexander Fleming")
]

history_questions = [
    ("Who was the first President of the United States?", "George Washington"),
    ("In which year did World War II end?", "1945"),
    ("Which ancient civilization built the pyramids?", "Ancient Egyptians"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What was the period in Europe known for renewed interest in art and learning?", "Renaissance"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("In what year did the Titanic sink?", "1912"),
    ("What event marked the beginning of World War I?", "Assassination of Archduke Franz Ferdinand"),
    ("Who was the longest-reigning British monarch?", "Queen Victoria"),
    ("Where was the Declaration of Independence signed?", "Philadelphia")
]

# Points for correct and incorrect answers
points_for_correct = 1
points_for_incorrect = 0

# Initialize counters
correct_answers = 0
incorrect_answers = 0

def quiz(category_questions):
    global correct_answers, incorrect_answers
    random.shuffle(category_questions)
    for question, correct_answer in category_questions[:10]:
        print(question)
        user_answer = input("Your answer: ")
        # Compare user's answer (considering case-insensitive comparison)
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
            incorrect_answers += 1

    print("Quiz completed!")
    total_score = correct_answers * points_for_correct - incorrect_answers * points_for_incorrect
    print(f"Your total score is: {total_score}")

# Main program
while True:
    print("Choose a category: ")
    print("1. Math")
    print("2. Science")
    print("3. History")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        quiz(math_questions)
    elif choice == '2':
        quiz(science_questions)
    elif choice == '3':
        quiz(history_questions)
    elif choice == '4':
        print("Quiz ended.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 to 4.")
