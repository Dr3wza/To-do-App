import time
import Functions
import PySimpleGUI as sg
import os

# Ensure todos.txt file exists
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# Check if image files exist
add_image_path = "004 add.png"
complete_image_path = "004 complete.png"
if not os.path.exists(add_image_path) or not os.path.exists(complete_image_path):
    sg.popup_error("Required images not found. Please ensure '004 add.png' and '004 complete.png' are in the working directory.")
    exit()

# Set up the GUI theme and layout
sg.theme("LightBlue")
clock = sg.Text(" ", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(image_source=add_image_path, mouseover_colors="Green", tooltip="Add Todo", key="Add")
list_of_todos = sg.Listbox(values=Functions.get_todos(), key="todos", enable_events=True, size=[50, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source=complete_image_path, key="Complete", mouseover_colors="Green")
exit_button = sg.Button("Exit")

# Define the window layout
layout = [
    [clock],
    [label, input_box, add_button],
    [list_of_todos, edit_button, complete_button],
    [sg.Push(), exit_button]
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 15))

# Event loop with clock update every 1 second
while True:
    event, values = window.read(timeout=1000)

    # Check if the window was closed
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # Update clock
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # Event handling
    match event:
        case "Add":
            new_todo = values["todo"].strip()  # Trim whitespace
            if new_todo:  # Validate non-empty input
                todos = Functions.get_todos()
                todos.append(new_todo + "\n")
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")  # Clear the input box
                sg.popup("To-do added successfully!", font=("Arial", 12))
            else:
                sg.popup("Please enter a to-do item before adding.", font=("Arial", 12))

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip()  # Trim whitespace
                if new_todo:
                    todos = Functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + "\n"
                    Functions.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")  # Clear the input box
                    sg.popup("To-do edited successfully!", font=("Arial", 12))
                else:
                    sg.popup("Please enter a new value for the selected to-do item.", font=("Arial", 12))
            except IndexError:
                sg.popup("Please select an item to edit.", font=("Arial", 12))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = Functions.get_todos()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")  # Clear the input box
                sg.popup("To-do completed and removed!", font=("Arial", 12))
            except IndexError:
                sg.popup("Please select an item to complete.", font=("Arial", 12))

        case 'todos':
            window["todo"].update(value=values["todos"][0])


window.close()
