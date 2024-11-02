user_prompt = "Enter a to do: "

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title)
    todos.append(todo)
