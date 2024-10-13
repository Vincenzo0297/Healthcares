# Import necessary module for input
from enum import Enum

class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

class Date:
    # Constructor
    def __init__(self, day=1, month=Month.Jan, year=2021):
        self.day = day
        self.month = month
        self.year = year

    # Accessor methods
    def get_Day(self):
        return self.day
    def get_Month(self):
        return self.month
    def get_year(self):
        return self.year
    
    # Mutator methods
    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class HealthProfile:
    # Constructor
    def __init__(self, firstName, lastName, Dob, Weight, Height, currentYear):
        self.firstName = firstName
        self.lastName = lastName
        self.Dob = Dob
        self.Weight = Weight
        self.Height = Height
        self.currentYear = currentYear
        
    # Accessor methods
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_Dob(self):
        return self.Dob
    def get_Weight(self):
        return self.Weight
    def get_Height(self):
        return self.Height
    def get_currentYear(self):
        return self.currentYear
    
    # Mutator methods
    def setfirstName(self, firstName):
        self.firstName = firstName
    def setlastName(self, lastName):
        self.lastName = lastName
    def setDob(self, Dob):
        self.Dob = Dob
    def setcurrentYear(self, currentYear):
        self.currentYear = currentYear
    def setBMIInformation(self, Weight, Height):
        self.Weight = Weight
        self.Height = Height
    
    # Non-static public methods
    def getAge(self):
        return self.currentYear - self.Dob.get_year()
    
    def getMaxHr(self):
        return 220 - self.getAge()
    
    def getMinTargetHR(self):
        return self.getMaxHr() * 0.50
    
    def getMaxTargetHR(self):
        return self.getMaxHr() * 0.85
    
    def getBMI(self):
        return self.Weight / (self.Height ** 2)
    
    def displayInformation(self):
        print(f"\nName: {self.firstName} {self.lastName}")
        print(f"Date of Birth: {self.Dob.get_Day()} {self.Dob.get_Month().name}, {self.Dob.get_year()}")
        print(f"Your weight: {self.Weight:.1f} kg")
        print(f"Your height: {self.Height:.1f} meters")
        print(f"Current Year: {self.currentYear}")
        print(f"Your age: {self.getAge()} years old\n")
        print(f"Clinic analysis, based on your age:")
        print(f"\t1. Your maximum heart rate is {self.getMaxHr()}")
        print(f"\t2. Your minimum target heart rate is {self.getMinTargetHR():.2f}")
        print(f"\t3. Your maximum target heart rate is {self.getMaxTargetHR():.2f}")
        print("\tWeight category             Range")
        print("\tUnderweight / too low       Below 18.5")
        print("\tHealthy range               18.5 - 25")
        print("\tOverweight                  25 - 30")
        print("\tObese                       30 - 35")
        print("\tSevere Obesity              35 - 40")
        print("\tMorbid Obesity              Over 40\n")


def main():
    with open("C:/Users/user/Desktop/New folder/patient.txt") as file:
        while True:
            # Read first name, check if it's empty to stop
            firstName = file.readline().strip()
            if not firstName:
                break  # End of file or no more patients

            # Continue reading patient data
            lastName = file.readline().strip()
            day = int(file.readline().strip())
            month = Month[file.readline().strip()]  # Read month as enum
            year = int(file.readline().strip())
            Weight = float(file.readline().strip())
            Height = float(file.readline().strip())
            currentYear = int(file.readline().strip())

            # Create Date and HealthProfile objects for the patient
            dob = Date(day, month, year)
            hp = HealthProfile(firstName, lastName, dob, Weight, Height, currentYear)

            # Display the patient's health profile information
            hp.displayInformation()

            # Skip the empty line between patients
            file.readline()

if __name__ == "__main__":
    main()


