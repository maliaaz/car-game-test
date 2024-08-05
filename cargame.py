command = ""
started = False
name = input("What's your name? ")
print(f"Hello {name}, welcome to Car Game! Type 'help' for instructions.")

while True:
    command = input(">").lower()
    if command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif command == "start":
        if not started:
            print("Car started...Ready to go!")
            started = True
        else:
            print("Car already started.")
    elif command == "stop":
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Car already stopped.")
    elif command == "quit":
        print(f"Thanks for playing, {name}!")
        break
    else:
        print("I don't understand that...")
