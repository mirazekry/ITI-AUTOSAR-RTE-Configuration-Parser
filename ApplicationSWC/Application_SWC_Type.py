import sys
sys.path.append('../')

from Base.BaseElement import BaseElement

# Description : This Class contains the Application SWC Type containers

class Application_SWC(BaseElement):

    def __init__(self,Name = None,Ports_List = [],InternalBehavoirs = []):

        super().__init__(Name)

        self.Ports              =   []
        self.InternalBehavoirs  =   []

        self.Ports.extend(Ports_List)
        self.InternalBehavoirs.extend(InternalBehavoirs)