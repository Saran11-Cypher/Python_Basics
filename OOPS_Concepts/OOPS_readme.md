## OOPS Concepts

#### What is a class?
- It is a template or a pattern through we can create many number of instances.
   
#### What is an Instance or an Object?
- It is a ouput product or else we can create something using the class templates.
  
#### What is an attribute and methods?
```python
class Anime:
    Name = "Naruto"
    Episodes = 90
    Power = 129
    def popularity():
        print("Naruto has best fanbase till Now")
anime = Anime()
print(anime.Name)
```
#### Explaination
- In the above example we can create inside the class **Anime**, we created the behaviours of Anime i.e., its **Name**,**Age** so it is called as **attributes**.
- After creating the attributes we created a *function* to print some values so this is called as **Methods**

#### What is a Constructor?

- A constructor is nothing but a method which is called immediately after creating an instance. 
- Through this constructor we can define so  many attributes in order to create instances.
- Example
  ```python
  class Anime:
    def __init__(self, Name, Episodes, Power):
        self.Name = Name
        self.Episodes = Episodes
        self.Power = Power
    def popularity():
        print(f"{self.Name} has best fanbase till Now")
  anime = Anime("Attack On Titans", 90, 1091)
  print(anime.Episodes)

#### Explaination
- So instead of creating the attributes one  by one we just created the attributes inside the constructor **def __init__**.
- Self represents the instance of the class. By using the **self**  we can access the attributes and methods of the class in Python. 
- **Self** binds the attributes with the given arguments.
- So when create an instance **anime = Anime()** it will provoke the **__init__** function then we can directly assign the values 
 Like this **anime = Anime("Attack on Titans", 90, 1091)**

### Types of OOPS:
1. Encapuslation
2. Polymorphism 
3. Inheritance
4. Abstraction
   
## Encapsulation
1. Setting up the private attributes ( Hidden from the user).
2. Using Getter and setter Concepts.
3. Mainly used to private purposes.


```python
class Anime:
    def __init__(self, Name, Episodes, Power, Rating):
    # As you can see here "self.name==>.name"is an variable assigned to the parameter "Name".
        self.name = Name 
        self.epi = Episodes
        self.pow = Power
        self.rat = Rating
        self.__char = "Jiraya"
    #Here the attribute named __char is not declared inside the function but we have created an attribute, its a private attribute meaning its hidden from the user.
    # **Self.__char ="Jiraya"
        
    def anime_character(self):
        print(f"{self.name} is the best Anime of all time")
        
    def get_character_name(self):
        print(f"{self.__char} is the main antagonist in {self.name}")
    #Here we are getting(return) after setting up the attribute(__char)
    def set_character_name(self, Character):
        self.__char = Character
    # In order to access this variable we have crea  ted getters and setters functions and in here we are set the value of that attribute.
        
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
```

## PolyMorphism
1. Polymorphism in OOP means **one thing, many forms**
2. Imagine a remote control that can work with different devices—TV, AC, or Music System. You press the **power** button, and it performs different actions depending on the device.
3. Similarly, in programming, polymorphism allows a single function or method to behave differently based on the object it is acting on.
   
4. ### Types of Polymorphism
   1. ### Compile Type PolyMorphism(Method  Overloading)
    - A class can have multiple methods with the same name but different parameters.
```python
class Bleach:
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

    def total_episodes(self,a,b,c):
        return a + b + c
    
    def print_total(self):
        print(f"Bleach has {self.total} views in this year")
        
ichigo = Bleach("Kurosaki", 1039, "Bankai", 329324,3240934, 234234234)
ichigo.print_total()       
```
### Code Explaination:
- In the above as we can see we used *args function over there, usually we can't implement Method overloading in python so that we are using the function named **args**
- Method overloading is nothing when we pass the number of paramters having same method name at the time of running the code the compiler will decide which method having the same parametres as the user given as input so these things will decide at the time of compilation.
- In this code we can give many number of inputs as we wish it will the outputs based on the number of inputs given to the methods.
- *As you can see I have declared the methods with the same name as **total_episodes** over there so in python it will considered the last given method (i.e the one which is declared at the last) so based on the parameters given in that the user have to give the values in this case.*
- In order to over come this issue **args** function is introduced in python
- The reason behind that we are using this kind of approach is that python is dynamic programming language.
  
   2. Run-time Polymorphism(Method Overriding):
   ```python
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
    ```
## Code Explaination
- AS you can see we created two same methods in two classes.
- As a parent class(Cars) which was inherited to the child Class (Lamboghirni) so all the properties of cars have been inherited tp Lamboghirni right?
- But when we declared the same method as in cars in Lambighirni and we create a instance for Lamboghirni and then we call the method(car_color) means it will take the method from child class not from parent class. 
- So the parent class method was completely over-ridden by the child class method.



## 3.   Inheritance
1. Class which inherits all the abilities from their parent class
2. We can reduce the code and resusability is high by using this concept.

```Python
class Cars:
    def __init__(self, Name, color):
        self.name = Name
        self.Col = color

class Lamboghini(Cars):
    engine = "V12 Engine"
    
class Ferrari(Cars):
    engine  = "V8 Engine"


class Electric_car(Lamboghini, Ferrari):
   pass

electric = Electric_car("Morris garages", "Green")
print(electric.engine)
```
## Code Explaination
1. As you can see **Car** is the child class here
2. **Lamboghini and Ferrari** are the child class for the class **Cars**
3. Here the class **Electric_car** is inherited from **Lamboghini and Ferrari** so when we create a same method with the same name in both **lamboghini and ferrari** and calls the function in **Electric_car** the one which calls in front will display output of the method. 
4. Here we can see **class Electric_car(Lamboghini, Ferrari)** Lamboghini is called first here so its method will display in the output of the instance electric.
5. suppose 
   ```python
   class Electric_car(Lamboghini, Ferrari):
       engine  = "Electric Engine"
    electric = Electric_car("Morris garages", "Green")
    print(electric.engine)
    ```
6. Here we declared the same name engine in this class also which means it will display the current **class Electric_car** method.


## 4. Abstraction
- process of hiding the implementation details and only showing the essential features of an object.
- It helps in reducing complexity and increases code maintainability.
```python
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
```

## Code Explaination
1. As you can see in this we are importing the **Abstract Class(ABC)** and **abstract method**.
2. In class **Anime** we created a template by declaring several methods so that we can modify the methods according to our needs in the child class like in this one**(Naruto)**.
3. The method which is having this syntax **@abstractmethod** is called as **Decorators** in python.
4. So when any of the methods is having this decorator in the parent class until or unless we defined that method in the child class, it cannot be inherited.
5. When we try to call the method from the parent class(Anime)
without creating that method in child class means we will face this error. ***Can't instantiate abstract class Naruto without an implementation for abstract methods 'anime_episodes', 'anime_genre', 'anime_name'***









   
   
