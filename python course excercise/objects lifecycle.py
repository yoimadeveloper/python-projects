class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'is king')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'will always be king', self.x)

class FootbllFan(PartyAnimal):
    points = 0
    def touchdowm(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)


an = FootbllFan("Mohit")
an.touchdowm()