class Tag:
    #Tag Class which contains only all arxml common needed tags of the AUTOSAR Schema

    inputParameters = 'PARAMETERS'
    inputReferences = 'REFERENCES'
    inputSubContainer= 'SUB-CONTAINERS'
    inputContainer = 'CONTAINERS'
    inputModule = 'Module'
    inputShortName = 'SHORT-NAME'
    inputDescription = 'DESC'
    generationValue  = 'VALUE'
    inputLowerMultiplicity = 'LOWER-MULTIPLICITY'
    inputUpperMultiplicity = 'UPPER-MULTIPLICITY'
    inputUpperMultiplicityInfinity = 'UPPER-MULTIPLICITY-INFINITE'
    inputEnumLiterals = 'ECUC-ENUMERATION-LITERAL-DEF'
    inputReferenceDestRef = 'DESTINATION-REF'
    '''output arxml common tags '''
    
    AUTOSAR="AUTOSAR"
    Packages="AR-PACKAGES"
    Package="AR-PACKAGE"
    Elements="ELEMENTS"
    ShortName="SHORT-NAME"
    ConfValues="ECUC-MODULE-CONFIGURATION-VALUES"
    Containers="CONTAINERS"
    DestinationRef = 'DESTINATION-REF'
    ConfContainerValue="ECUC-PARAM-CONF-CONTAINER"
    ChoiceContainerValue = "ECUC-CHOICE-CONTAINER"
    ParameterValues="PARAMETER-VALUES"
    NumericalValue="ECUC-INTEGER-PARAM-VALUE"
    FloatValue="ECUC-FLOAT-PARAM-VALUE"
    FunctionNameValue = "ECUC-FUNCTION-NAME-VALUE"
    StringValue="ECUC-STRING-PARAM-VALUE"
    BooleanValue="ECUC-BOOLEAN-PARAM-VALUE"
    EnumerartionValue="ECUC-ENUMERATION-PARAM-VALUE"
    Value="VALUE"
    RefernceValue = 'REFERENCE-VALUES'
    RefInfoTag = 'ECUC-REFERENCE'
    DestinationRef = 'DESTINATION-REF'
    SubContainer="SUB-CONTAINERS"
    Choices = "CHOICES"