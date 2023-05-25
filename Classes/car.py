class Car:
    fuel_type = "petrol"
    def __init__(self,make,color,model):
        self.color = color
        self.make = make
        self.model = model
    def start_start(self):
     return f"Vroom I am a {self.color}, {self.make},{self.model}"

    def show_color_make(self):
     return f"It is classy being a {self.color},{self.make},{self.model}"

    def car_model(self):
      return self.model
    
 