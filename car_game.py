from audioop import reverse


intro ='''(i)   Enter "start" to start the car.
          (ii)  Enter "stop" to stop the car.
          (iii) Enter "quit" to quit the car.
          '''
print(intro)
start = input("Enter your command : ")
start = start.strip()
start = start.lower()

while start == "start" or start == "stop":
        if start == "start":
            print("car is started.")
            temp = start
        elif start == "stop":
            print("car is stopped.")
            temp = start
        
        start = input("Enter your command : ")
        while temp == start:
            if start == "start":
                print("car is already started")
                break
            else:
                print("car is already stopped")
                break
        break
else:
        if start == "quit":
            print("Game is stopped.")
        else:
            print("Invaild command.")
