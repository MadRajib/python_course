class Particles :
    roar =" i am a particle"

    def __init__(self):
        self.c = 0
        self.m = 0
        self.r = {'x':0,'y':0,'z':0}

    def tellmass(self):
        print(self.m)
        print(self.roar)

higgs = Particles()

# instance variable
higgs.name = "Boson"

print(higgs.roar)
print(higgs.name)

higgs.tellmass()