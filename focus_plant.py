import time

plant_stages = [
    """
      .
    """,
    """
      .
      |
    """,
    """
      .
      |
     / \\
    """,
    """
      .
      |
     / \\
    /   \\
    """,
    """
      .
      |
     / \\
    /   \\
     | |
    """,
    """
       🌱
       |
      / \\
     /   \\
      | |
    """
]

growth = 0

def start_focus_session():
    global growth
    minutes = int(input("Focus minutes: "))
    seconds = minutes * 60

    print("Focus session started. Stay on task 🌿")

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"Time left: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nSession complete! Your plant grew 🌱")
    if growth < len(plant_stages) - 1:
        growth += 1

def show_plant():
    print("\nYour focus plant:")
    print(plant_stages[growth])

while True:
    print("\n1. Start focus session")
    print("2. View plant")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        start_focus_session()
    elif choice == "2":
        show_plant()
    elif choice == "3":
        print("Keep growing 🌿")
        break
    else:
        print("Invalid choice")
