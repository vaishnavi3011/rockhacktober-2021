class Car():
    def __init__(self, name , model, year):
        """give the name model and year"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0
    def describe(self):
       """it will give the describtion"""
       print("Name of car : " + self.name + "\n" + "Year of Build: " + str(self.year))
       print("Model name : "+ self.model)
    def odometerRead(self):
       print("Odometer read : " + str(self.odometer))
    def odometerUpadate(self, read):
        if read >= self.odometer:
             print(f"odometr upadate : {read}")
             self.odometer = read
        else: 
             print("cant roll back the odometer")
    def incrementOdometer(self, increment):
         if increment > 0:
            self.odometer += increment
         else:
            print(" increment cant be negative") 
    def Gastype(self):
        print("petrol")

class electricCar(Car):
    def __init__(self,name,model, year):
        super().__init__(name,model,year)
        self.battry = 70
    def describeBattery(self):
        print(f"The battery capacity : {self.battry}kh")    