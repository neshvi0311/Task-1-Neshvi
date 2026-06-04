import random

questions = [
    ("What is the capital of India?", "Delhi"),
    ("Which is the national animal of India?", "Tiger"),
    ("Which is the national bird of India?", "Peacock"),
    ("What is the national flower of India?", "Lotus"),
    ("Who is known as the Father of the Nation?", "Gandhi"),
    ("Which state is known as the Land of Five Rivers?", "Punjab"),
    ("Which is the largest state in India by area?", "Rajasthan"),
    ("Which Indian city is known as the Pink City?", "Jaipur"),
    ("What is the currency of India?", "Rupee"),
    ("Who wrote the Indian National Anthem?", "Tagore"),
    ("Which river is known as the Ganga of the South?", "Godavari"),
    ("What is the national sport of India?", "Hockey"),
    ("Which is the highest mountain peak in India?", "Kanchenjunga"),
    ("Which Indian state has the longest coastline?", "Gujarat"),
    ("Who was the first Prime Minister of India?", "Nehru"),
    ("Which is the smallest state in India by area?", "Goa"),
    ("What is the national tree of India?", "Banyan"),
    ("Which monument is known as the symbol of love?", "Taj Mahal"),
    ("Which Indian organization launched Chandrayaan missions?", "ISRO"),
    ("What is the national aquatic animal of India?", "Dolphin")
]

score = 0

print("=" * 50)
print("         INDIA GENERAL KNOWLEDGE QUIZ")
print("=" * 50)

selected_questions = random.sample(questions, 5)

for i, (question, answer) in enumerate(selected_questions, start=1):

    print(f"\nQuestion {i}")
    user_answer = input(question + " : ")

    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {answer}")

print("\n" + "=" * 50)
print(f"Final Score: {score}/5")
print("=" * 50)

if score == 5:
    print("🏆 Excellent! Perfect Score.")
elif score >= 3:
    print("👍 Good Job!")
else:
    print("📚 Keep Learning and Try Again!")