import random
from termcolor import colored, cprint

# define vehicle class - parent class
class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    def setMake(self, make):
        self.make = make        

    def setModel(self, mode):
        self.mode = mode      

    def setYear(self, year):
        self.year = year      

    def setWeight(self, weight):
        self.weight = weight      
    
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight
    
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving
    
    def drive(self):
        self.isDriving = True
    
    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False

class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = isFlying
    
    def flying(self):
        if self.needsMaintenance == True:
            return False
        self.isFlying = True
        return True
    
    def landing(self):
        if self.isFlying:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isFlying = False


def drive_car(car):
    drive_times = random.randint(1, 101)
    for i in range(drive_times):
        car.drive()
        car.stop()

def fly_plane(plane, fly_times = None):
    fly_times = random.randint(1, 101) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = plane.flying()
        if is_flying:
            plane.landing()
        else:
            cprint("plane " + plane.model + " can't fly until it's repair", 'red', attrs=['bold'])
            cprint("Repairing... " + plane.model, 'blue', attrs=['bold'])
            plane.repair()
       
def print_car_specs(car):
    print("========================")
    print('Make ',car.make)
    print('Model ',car.model)
    print('Year ',car.year)
    print('Weight ',car.weight)
    print('Needs Maintenance ',car.needsMaintenance)
    print('Trips Since Maintenance ',car.tripsSinceMaintenance)
    print('Weight ',car.weight)
    print("========================\n")

def print_plane_specs(plane):
    print("========================")
    print('Make ',plane.make)
    print('Model ',plane.model)
    print('Year ',plane.year)
    print('Weight ',plane.weight)
    print('Needs Maintenance ',plane.needsMaintenance)
    print('Trips Since Maintenance ',plane.tripsSinceMaintenance)
    print('Weight ',plane.weight)
    print("========================\n")

carOne = Cars("Mahindra", "XUV500", 2015, 1860 )
carTwo = Cars("Mahindra", "XUV300", 2018, 1404 )
carThree = Cars("Mahindra", "Thar", 2020, 1750 )

planeOne = Plane("Oman Air","Boeing 737", 1997, 183500)
planeTwo = Plane("Oman Air","Air Bus A380", 2005, 575000)

drive_car(carOne)
drive_car(carTwo)
drive_car(carThree)
fly_plane(planeOne)
fly_plane(planeTwo, 102)

print_car_specs(carOne)
print_car_specs(carTwo)
print_car_specs(carThree)
print_plane_specs(planeOne)
print_plane_specs(planeTwo)
