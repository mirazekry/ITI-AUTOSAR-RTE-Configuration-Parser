import sys
sys.path.append('../')

from Base.BaseElement import BaseElement

# Description : This class contains Runnable specification

class Runnable(BaseElement):

    def __init__(self,Name = None,Can_Be_Invojked_Concurrently = 'false',Minmum_Start_Intrval = None,Symbol = None):

        super().__init__(Name)

        self.Can_Be_Invojked_Concurrently = Can_Be_Invojked_Concurrently
        self.Minmum_Start_Intrval         = Minmum_Start_Intrval
        self.Symbol                       = Symbol
    