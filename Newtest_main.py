

import os
import xml.etree.ElementTree as ET


from Major_Package_Parser import Major_Package_Parser
from Major_Package import Major_Package


PackageObject = Major_Package_Parser()
# PackageObject.getPackage(moduleSchemaShortName='SeatHeater'):
    
test_Pack= Major_Package_Parser(Major_PackageRootTag=PackageObject.getPackage(moduleSchemaShortName='SeatHeater') )

m=test_Pack.getObjects('DataTypes')

for element in m:
    print(element.getParameterInfo())
#print('objec :',m)




