text = input()

while True:
    if text == "start":
        print("Starting program...")
    elif text == "stop":
        print("Program has stopped...")
        break
    print("text: {}".format(text))
    text = input()
