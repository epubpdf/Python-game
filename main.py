import random

def run():
    print("   Pick an option: ")
    print("Enter R for Rook")
    print("Enter P for Paper")
    print("Enter S for Scissors")
    Player = ["r","p","s"]
    Player = input("Enter your pick?: ")

    return Player

while True:
    Player = run().lower()

    CPU = random.choice(["r","p","s"])

    if Player == "r":
        if CPU == "p":
            print("CPU: (Paper)")
            print("Player: (Rook)" )
            print("CPU has won!")
            break
    
    if CPU == "s":
        print("CPU: (Scissors)")
        print("Player: (Rook)")
        print("You have won!")
        break
    elif Player == "s":
        if CPU == "r":
            print("CPU: (Rook)")
            print("Player: (Scissors)")
            print("CPU has won!")
            break
        if CPU == "p":
            print("CPU: (Paper)")
            print("Player: (Scissors)")
            print("You have won!")
            break

    elif Player == "p":
        if CPU == "s":
            print("CPU: (Scissors)")
            print("Player: (Paper)")
            print("CPU has won!")
            break
        if CPU == "r":
            print("CPU: (Rook)")
            print("Player: (Paper)")
            print("You have won!")
            break

    elif Player == CPU:
        print("CPU: ",(CPU))
        print("Player: ",(Player))
        print("It is a tie!")
        
    else:
        print("Invalid input, Please enter a valid option!")