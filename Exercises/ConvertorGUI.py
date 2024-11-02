import PySimpleGUI as GUI

GUI.theme("LightBlue")
label1 = GUI.Text("Enter Feet")
input1 = GUI.Input(key="feet")

label2 = GUI.Text("Enter Inches")
input2 = GUI.Input(key="inches")

convert_button = GUI.Button("Convert", key="meters")
label3 = GUI.Text(" ", key="output") # Start with an empty label for output
exit_button = GUI.Button("Exit", key="terminate")

col1 = GUI.Column([[label1], [label2]])
col2 = GUI.Column([[input1], [input2]])

# GUI.Push() moves exit button to the far right
window = GUI.Window("Convertor", [[col1, col2],
                                  [convert_button,
                                   label3, GUI.Push(), exit_button]])

while True:
    event, values = window.read()

    if event == "meters":
        try:
            # Convert feet and inches to meters
            feet = float(values["feet"])
            inches = float(values["inches"])
            result = feet * 0.3048 + inches * 0.0254

            # Update the output label with formatted result
            window["output"].update(f"{result:.2f} meters")
        except ValueError:
            GUI.popup("Please provide two numbers")

    if event == "terminate" or event == GUI.WIN_CLOSED:
        break

window.close()