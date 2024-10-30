import Functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_of_todos = sg.Listbox(values=Functions.get_todos(),
                           key="todos", enable_events=True,
                           size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label, input_box, add_button],
                           [list_of_todos, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

# x, y = (event, value)
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])

    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            # The '0' gives only the string
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = Functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            Functions.write_todos(todos)
            window["todos"].update(values=todos)

        case 'todos':
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = Functions.get_todos()
            todos.remove(todo_to_complete)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value=" ")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
