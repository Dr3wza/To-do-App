import PySimpleGUI as sg
import ZIP_creator


label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
# Changed to `FilesBrowse` for multiple file selection
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    if event == "Compress":
        # Split paths in case of multiple files selected
        filepaths = values["files"].split(";")
        folder = values["folder"]
        ZIP_creator.make_archive(filepaths, folder)
        # window["output"].update(value="Compression Completed")
        sg.popup("Compression Complete", "Your files have been compressed!")

    if event == sg.WINDOW_CLOSED:
        break


window.close()
