import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.bowlers = []

    def select_captain(self, player):
        self.captain = player

    def set_batting_order(self, batting_order):
        self.batting_order = batting_order

    def choose_bowler(self):
        return random.choice(self.bowlers)

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def simulate_ball(self):
        batsman = self.team1.batting_order[0]
        bowler = self.team2.choose_bowler()
        boundary_probability = batsman.batting * (1 - bowler.bowling)
        out_probability = (1 - batsman.fielding) * bowler.bowling

        if random.random() < boundary_probability:
            self.score += 4
            commentary = f"{batsman.name} hits a boundary!"
        elif random.random() < out_probability:
            self.wickets += 1
            commentary = f"{batsman.name} is out!"
            self.team1.batting_order.pop(0)
        else:
            self.score += 1
            commentary = "A single run scored."

        self.overs += 0.1
        self.team1.batting_order.append(self.team1.batting_order.pop(0))

        return commentary

class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def provide_commentary(self):
        commentary = self.umpire.simulate_ball()
        print(commentary)

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(team1, team2, field)
        self.commentator = Commentator(self.umpire)

    def start_match(self):
        print("Match started!")
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.set_batting_order(random.sample(self.team1.players, len(self.team1.players)))
        self.team2.set_batting_order(random.sample(self.team2.players, len(self.team2.players)))

        for player in self.team1.players:
            if player != self.team1.captain:
                self.team1.bowlers.append(player)

        for player in self.team2.players:
            if player != self.team2.captain:
                self.team2.bowlers.append(player)

        while self.umpire.overs < 5:
            self.commentator.provide_commentary()

        self.end_match()

    def end_match(self):
        print("Match ended!")
        print(f"Final Score: {self.umpire.score}/{self.umpire.wickets}")

# Example usage
player1 = Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.1, 0.9, 0.95, 0.7, 0.8)
player3 = Player("Rohit Sharma", 0.1, 0.85, 0.9, 0.75, 0.7)
team1 = Team("Team 1", [player1, player2, player3])

player4 = Player("Kane Williamson", 0.15, 0.75, 0.96, 0.8, 0.85)
player5 = Player("Steve Smith", 0.2, 0.85, 0.93, 0.7, 0.75)
player6 = Player("Joe Root", 0.15, 0.8, 0.92, 0.75, 0.8)
team2 = Team("Team 2", [player4, player5, player6])

field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
match.start_match()
