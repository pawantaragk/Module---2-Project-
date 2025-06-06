import time

def focus_timer(minutes):
    """Simple focus timer with countdown"""
    seconds = minutes * 60
    print(f"\nFocus time started for {minutes} minutes!")
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f" {mins:02d}:{secs:02d} remaining", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\n Time's up! Take a break!")
    # Play system beep
    print("\a")

def main():
    print(" Simple Time Manager ")
    while True:
        print("\n1. Start focus session")
        print("2. Exit")
        choice = input("Choose (1/2): ")
        
        if choice == "1":
            try:
                mins = int(input("Enter minutes to focus: "))
                focus_timer(mins)
            except:
                print("Please enter a number!")
        elif choice == "2":
            print("Goodbye! Stay productive!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()