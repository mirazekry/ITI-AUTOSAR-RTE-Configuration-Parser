import sys
sys.path.append('../')
# Description : This class contains the basic data for all objects

class BaseElement:

    Name = None             #Holds The name of the object

    def __init__(self,Name = None):
        if Name:
            self.Name = Name
