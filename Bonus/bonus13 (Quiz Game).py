import json

#  This turns the json file into a long string
with open("questions.json", "r") as file:
    content = file.read()

# This turns the string into a list with 2 entries (questions)
# loads = load string
data = json.loads(content)

# question is the dictionary within the list "data"
for question in data:
    print(question["question_text"])
    for index, Answer in enumerate(question["Answers"]):
        print(index +1, "-", Answer)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = (f"{index + 1} - {result}! Your answer: {question['user_choice']}, "
               f"Correct answer: {question['correct_answer']}")
    print(message)

print(score, "/", len(data))

