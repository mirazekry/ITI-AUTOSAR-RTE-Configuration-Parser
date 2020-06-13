#new


class Element:
    #Elements class contains all parameter's related info
    
    shortName           = None  #Holds the shortname of the parameter
  
    def __init__(self,shortName=None
                 ):
        #Elements Class constructor function

        if shortName:
            self.shortName    = shortName
  



    def getParameterInfo(self):
        #Function which returns all Elements's info as a dict

        return {
            'SHORT-NAME':self.shortName,
        }
   

    def setShortName(self,shortName):
        self.shortName=shortName



   

