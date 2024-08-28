from Core import DemoBaseModule

class OperatorDemo(DemoBaseModule.DemoBase):
    def __init__(self) -> None:
        super().__init__("Operator Demo")
        
    def Demo(self):
        print(f'1+2: {1+2}')
        print(f'1-2: {1-2}')
        print(f'1/2: {1/2}')
        print(f'3*2: {3*2}')
        print(f'3%2: {3%2}')
        print(f'3**2 (3^2): {3**2}')
        print(f'3 == 2: {3==2}')
        print(f'3 > 2: {3>2}')