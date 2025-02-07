class Anime:
    def __init__(self, Name, Episodes, Power, Rating):
    # As you can see here "self.name==>.name"is an variable assigned to the parameter "Name".
        self.name = Name 
        self.epi = Episodes
        self.pow = Power
        self.rat = Rating
        self.__char = "Jiraya"
        
    def anime_character(self):
        print(f"{self.name} is the best Anime of all time")
        
    def get_character_name(self):
        print(f"{self.__char} is the main antagonist in {self.name}")
        
    def set_character_name(self, Character):
        self.__char = Character
        
    def anime_with_higherpower(self, total):
        print(f"{self.name} has highest power character", total)
        
    def __del__(self):
        print("This is a destructor", self) 
        
    def __str__(self):
        return(f"{self.epi}")

anime = Anime("Bleach", 156, 190.98, 100)
print(anime.name) #Hence we have the attribute from the variable that we named rat, so the variable doesn't matter that we can give any name.
print(anime)
anime.anime_with_higherpower(908)
anime.get_character_name()
anime.set_character_name("Itachi")
anime.get_character_name()


