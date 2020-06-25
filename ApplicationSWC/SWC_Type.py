import sys
sys.path.append('../')

from Base.BaseElement import BaseElement

# Description : This Class contains the Application SWC Type containers

class SWC(BaseElement):

    def __init__(self,Name = None,Type = None,Ports_List = [],InternalBehavoirs = []):

        super().__init__(Name)
        self.Type               =  Type
        self.Ports              =   []
        self.InternalBehavoirs  =   []

        self.Ports.extend(Ports_List)
        self.InternalBehavoirs.extend(InternalBehavoirs)