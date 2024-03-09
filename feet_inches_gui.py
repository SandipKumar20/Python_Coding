import PySimpleGUI as sg


def convert(feet_, inches_):
    """ Function which converts feet and inches to meters."""
    meters = feet_ * 0.3048 + inches_ * 0.0254
    return meters


feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches;")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],[inches_label, inches_input],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = convert(feet, inches)
    result = round(result, 2)
    window["output"].update(value=f"{result} meters", text_color="white")
window.close()