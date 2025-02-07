from abc import ABC, abstractmethod

class Anime(ABC):
    @abstractmethod
    def anime_name(self):
        pass
    
    @abstractmethod
    def anime_episodes(self):
        pass
    
    @abstractmethod
    def anime_genre(self):
        pass
class Naruto(Anime):
    def __init__(self, Name):
        self.value = Name
    def anime_name(self, name):
        name = "Itachi"
        print(f"Anime is called as {self.value}",name)

nau = Naruto()
nau.anime_episodes()
# Can't instantiate abstract class Naruto without an implementation for abstract methods 'anime_episodes', 'anime_genre', 'anime_name'