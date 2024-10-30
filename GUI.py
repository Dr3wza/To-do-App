import time
import Functions
import PySimpleGUI as sg

sg.theme("Black")
clock = sg.Text(" ", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=10)
list_of_todos = sg.Listbox(values=Functions.get_todos(),
                           key="todos", enable_events=True,
                           size=[50, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label, input_box, add_button],
                           [list_of_todos, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

# x, y = (event, value)
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])

    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                # The '0' gives only the string
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = Functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Arial", 20))

        case 'todos':
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = Functions.get_todos()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value=" ")
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Arial", 20))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
