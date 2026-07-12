# Quiz Game in Python

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for AI and Machine Learning?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "5. Which data type stores True or False values?",
        "options": ["A. int", "B. bool", "C. float", "D. string"],
        "answer": "B"
    }
]

score = 0

print("=" * 40)
print("      Welcome to the Quiz Game")
print("=" * 40)

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

print("\n" + "=" * 40)
print("Quiz Completed!")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("🏆 Excellent! Perfect Score!")
elif percentage >= 80:
    print("🎉 Great Job!")
elif percentage >= 60:
    print("👍 Good Work!")
else:
    print("📚 Keep Practicing!")

print("=" * 40)