class User:

    def __init__(self, name, games_won, games_lost, games_drawn, no_of_rounds):
        self.name = name;
        self.games_won = games_won;
        self.games_lost = games_lost;
        self.games_drawn = games_drawn;
        self.no_of_rounds = no_of_rounds;

    def show(self):
        print('Name: ',self.name , ' games_won: ',self.games_won ,' games_lost ', self.games_lost, ' games_drawn: ' ,self.games_drawn);