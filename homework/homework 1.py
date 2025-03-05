class hero:
    def __init__(self , name , lvl , HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP
    def introduce(self):
        print (f'My name is {self.name} . My level is {self.lvl}. My HP {self.HP}')
    def is_adult(self):
        return self.lvl >= 10
hero1 = hero("Supermen",15,98)
hero2 = hero("Batmen",11, 88)
hero3 = hero("Cap",8,25)
(hero1.introduce())
print(hero1.is_adult())
(hero2.introduce())
print(hero2.is_adult())
(hero3.introduce())
print(hero3.is_adult())