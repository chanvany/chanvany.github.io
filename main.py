import random

def quiz():
    questions = [
        {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": "Paris"},
        {"question": "What is the highest mountain in the world?", "options": ["K2", "Kangchenjunga", "Lhotse", "Mount Everest"], "answer": "Mount Everest"},
        {"question": "What is the smallest country in the world?", "options": ["Monaco", "Nauru", "Tuvalu", "Vatican City"], "answer": "Vatican City"},
        {"question": "What is the largest ocean in the world?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
        {"question": "What is the name of the planet closest to the sun?", "options": ["Venus", "Mars", "Mercury", "Jupiter"], "answer": "Mercury"},
        {"question": "Who painted the Mona Lisa?", "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "answer": "Leonardo da Vinci"},
        {"question": "What is the currency of Japan?", "options": ["Yuan", "Yen", "Won", "Rupee"], "answer": "Yen"},
        {"question": "What is the largest country in the world by land area?", "options": ["China", "Russia", "Canada", "United States"], "answer": "Russia"},
        {"question": "What is the name of the largest desert in the world?", "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Polar Desert"], "answer": "Antarctic Polar Desert"},
        {"question": "What is the chemical symbol for gold?", "options": ["Ag", "Au", "Fe", "Hg"], "answer": "Au"}
    ]

    score = 0
    for question in random.sample(questions, 10):
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Your answer (1-4): ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                if question["options"][user_answer - 1] == question["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is: {question['answer']}")
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYou got {score} out of 10 questions correct.")

quiz()
    
