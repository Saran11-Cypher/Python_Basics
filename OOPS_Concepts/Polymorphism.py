class Bleach:
#Method Overloading (Compile Time polymorphism)
    def __init__(self, Name, episodes, character, *args):
        self.name = Name
        self.number = episodes
        self.char = character
        self.total = self.total_episodes(*args)
        
    def total_episodes(self, *args):
        sum = 0
        for i in args:
            sum +=i
        return sum
    
    def print_total(self):
        print(f"Bleach has {self.total} views in this year")
        
ichigo = Bleach("Kurosaki", 1039, "Bankai", 329324,3240934, 234234234, 3243234)
ichigo.print_total()

# Run-time Polymorphism
class Cars:
    def __init__(self, Name, Color):
        self.name = Name
        self.color = Color
        
    def car_color(self):
        print(f"This car color is {self.color}")
        
class Lamboghirni(Cars):
    def car_color(self):
        print(f"This is a child class method and this car color is {self.color}")
        
lambo  = Lamboghirni("Murcielogo", "Blood_red")
lambo.car_color()
        

    

    
        
        