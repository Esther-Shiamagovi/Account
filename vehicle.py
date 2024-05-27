class Vehicle:
    def __init__(self,model,make):
        self.model=model
        self.make=make
        
    def move(self):
            print("The vehicle is moving")
            
class Bus(Vehicle):
    def __init__(self,model,make,capacity) :
        super().__init__(model,make)
        self.capacity=capacity
        
    def hoot(self):
        print("The bus is hooting")
    def check_capacity(self):
        print(f"The capasity is {self.capacity}")

class Lorry(Vehicle):
    def __init__(self, model, make,load_weight):
        super().__init__(model, make)
        self.load =load_weight
        
    def unload(self):
        print("Unloading the load")
        
    
        
        

        

        
        
    
    
