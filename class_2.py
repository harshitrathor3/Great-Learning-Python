class Phone:
    def set_color(self,color,cost):
        self.color=color
        self.cost=cost
    #def set_cost(self,cost):
        #self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Making Phone Call")
    def play_game(self):
        print("Playing Games")
