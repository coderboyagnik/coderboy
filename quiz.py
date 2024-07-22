def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the color of the sky?": "Blue"
    }
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your score: {score}/{len(questions)}")

quiz()
