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