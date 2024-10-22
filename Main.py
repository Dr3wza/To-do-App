# from Functions import get_todos, write_todos
import Functions
import time

now = time.strftime("%d %B %Y, %H:%M")
print("Date & Time:", now)


while True:
    # Get user input and remove space characters from input
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = Functions.get_todos()
        todos.append(todo + "\n")
        Functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = Functions.get_todos()
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = Functions.get_todos()
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + "\n"
            Functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. Enter the associated number with the to-do item")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = Functions.get_todos()
            index = number - 1
            todo_removed = todos[index].strip('\n')
            todos.pop(index)
            Functions.write_todos(todos)
            message = f"Todo '{todo_removed}' was removed"
            print(message)

        except ValueError:
            print("Your command is not valid. Enter the associated number with the to-do item")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye")
