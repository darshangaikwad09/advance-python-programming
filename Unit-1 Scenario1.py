class Player:
    def __init__(self, name, jersey, runs):
        self.name = name
        self.jersey = jersey
        self.runs = runs

    def category(self):
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 200:
            return "Good"
        return "Average"

    def display(self):
        print("\nPlayer Name :", self.name)
        print("Jersey Number :", self.jersey)
        print("Runs :", self.runs)
        print("Category :", self.category())


class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter Player Name: ")
        jersey = int(input("Enter Jersey Number: "))
        runs = int(input("Enter Runs: "))
        self.players.append(Player(name, jersey, runs))
        print("Player Added Successfully!")

    def display_players(self):
        if len(self.players) == 0:
            print("No players available.")
        else:
            i = 0
            while i < len(self.players):
                self.players[i].display()
                i += 1


team = Team()

while True:
    print("\n1. Add Player")
    print("2. Display All Players")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        team.add_player()
    elif choice == 2:
        team.display_players()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
