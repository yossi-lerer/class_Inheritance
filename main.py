# step 1 -  Swimmer Inherits from Athlete
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")

class Swimmer(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age)

tom = Swimmer("Tom", 22)
tom.introduce()

# step 2 - Runner with a Fixed Sport
class Athlete:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport
    def describe(self):
        print(f"{self.name} competes in {self.sport}.")
class Runner(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age, "Running")
sara = Runner("Sara", 25)
sara.describe()

# step 3 - Cyclist with Gear Info
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")
class Cyclist(Athlete):
    def __init__(self, name, age, bike_brand):
        super().__init__(name, age)
        self.bike_brand = bike_brand
    def describe_gear(self):
        print(f"Cyclist {self.name} rides a {self.bike_brand}.")
mike = Cyclist("Mike", 30, "Trek")
mike.introduce()
mike.describe_gear()
# step 4 - Three Sports, One Parent
class Athlete:
    def __init__(self, name, country, stroke = None):
        self.name = name
        self.country = country 
    def greet(self):
        return f"{self.name} represents {self.country}."
class Swimmer(Athlete):
    def __init__(self, name, country, stroke_style):
        super().__init__(name, country)
        self.stroke_style = stroke_style
class Runner(Athlete):
    def __init__(self, name, country, best_distance):
        super().__init__(name, country)
        self.best_distance = best_distance
class Cyclist(Athlete):
    def __init__(self, name, country, race_type):
        super().__init__(name, country,)
        self.race_type = race_type

lior = Swimmer("Lior", "Israel", "freestyle")
avi = Runner("Avi", "Kenya", "marathon") 
jan = Cyclist("Jan", "France", "road")
print(lior.greet())
print(avi.greet())
print(jan.greet())
# step 5 - Shared Warm-Up Method
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def warm_up(self):
        return f"{self.name} is warming up."
class Gymnast(Athlete):
    def __init__(self, name, age, apparatus):
        super().__init__(name, age)
        self.apparatus = apparatus
    def compete(self):
        print(f"{self.name} competes on the {self.apparatus}")
class Swimmer(Athlete):
    def __init__(self, name, age, stroke):
        super().__init__(name, age)
        self.stroke = stroke
    def compete(self):
        print(f"{self.name} competes on the {self.stroke}")
ana = Gymnast("Ana", 19, "rings")
ben = Swimmer("Ben", 21, "butterfly")
print(ana.warm_up())
ana.compete()
print(ben.warm_up())
ben.compete()
# step 6 - Constructor Chaining with super()
class Athlete:
    def __init__(self, name, age, years_active):
        self.name = name
        self.age = age
        self.years_active = years_active
    def experience(self):
        return f"{self.name} has been active for {self.years_active} years."
class TeamSportPlayer(Athlete):
    def __init__(self, name, age, years_active, team_name):
        super().__init__(name, age, years_active)
        self.team_name = team_name
    def team_info(self):
        print(f"{self.name} plays for {self.team_name}.")
gal = TeamSportPlayer("Gal", 28, 10, "Maccabi")
print(gal.experience())
gal.team_info()
# step 7 - Personal Best Tracking
class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.personal_best = None
    def set_record(self, value):
        self.personal_best = value
        return self.personal_best
    def has_record(self):
        return  self.personal_best != None
class Sprinter(Athlete):
    def __init__(self, name):
        super().__init__(name, "100m Sprint")
usain = Sprinter("Usain") 
print(usain.has_record())
print(usain.set_record(10.8))
print(usain.has_record())
# step 8 - Training Session Counter
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions_completed = 0
    def train(self):
        self.sessions_completed += 1
        return self.sessions_completed
    def sessions_needed(self, target):
        if target - self.sessions_completed >= 0:
            return target - self.sessions_completed
        else:
            return 0
class Triathlete(Athlete):
    def __init__(self, name, age, discipline):
        super().__init__(name, age)
        self.discipline = discipline
    def describe(self):
        print(f"Triathlete {self.name}, age {self.age}, discipline: {self.discipline}")
dan = Triathlete("Dan", 26, "cycling")
dan.describe()
print(dan.train(), " sessions completed")
print(dan.train(), " sessions completed")
print(dan.train(), " sessions completed")
print(dan.train(), " sessions completed")
print(dan.train(), " sessions completed")
print(dan.sessions_needed(10), " more needed")
# step 9 - Basketball Player Card
class Athlete:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    def player_card(self):
        print(f"player card: \nname: {self.name} \nage: {self.age} \nposition: {self.position}")
class BasketballPlayer(Athlete):
    def __init__(self, name, age, position, jersey_number):
        super().__init__(name, age, position)
        self.jersey_number = jersey_number
    def full_profile(self):
        self.player_card()
        print(f"Jersey: #{self.jersey_number}")
mia = BasketballPlayer("Mia", 24, "guard", 7)
mia.full_profile()
mosh = BasketballPlayer("Mosh", 15, "gk", 6)
mosh.full_profile()
ori = BasketballPlayer("ori", 19, "cmd", 8)
ori.full_profile()
# step 10 - Three-Level Inheritance Chain
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi, I am {self.name}.")
class Athlete(Person):
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport
    def train(self):
        print(f"{self.name} is training for {self.sport}.")
class ProfessionalAthlete(Athlete):
    def __init__(self, name, age, sport, sponsor):
        super().__init__(name, age, sport)
        self.sponsor = sponsor
    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponsor}.")
ronaldo = ProfessionalAthlete("Ronaldo", 39, "football", "Nike")
ronaldo.greet()
ronaldo.train()
ronaldo.sponsor_info()
# self learn
# step 1 
class Logger:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
test1 = Logger()
test2 = Logger()
print(test1 is test2)