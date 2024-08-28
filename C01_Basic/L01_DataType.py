from Core import DemoBaseModule

class DataTypeDemo(DemoBaseModule.DemoBase):
    def __init__(self) -> None:
        super().__init__("Data Type Demo")
        
    def Demo(self):
        boolVal = True
        print(f"boolVal: {boolVal}")
        
        intVal = 5
        print(f"intVal: {intVal}")
        
        floatVal = 5.5
        print(f"floatVal: {floatVal}")
        
        stringVal = "Hello"
        print(f"string: {stringVal}")
        
        listVal = [1,2,"Anything", 4.5, 'X']
        print(f"listVal: {listVal}")
        
        dictVal = {"key1": 1, "key2": 2, "key3":"StringVal"}
        print(f"dictVal: {dictVal}")
        
        tupleVal = (10, "A", "C", 5.5)
        print(f"tupleVal: {tupleVal}")
        
        setVal = {1,2,3,4,"5"}
        print(f"setVal: {setVal}")
        