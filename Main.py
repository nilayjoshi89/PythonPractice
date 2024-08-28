from operator import truediv
from Core import FactoryModule
from Core.DemoBaseModule import DemoBase

def PrintAvailableDemos(demoDict: dict) -> None:
    print(f"Available Demos:")
    for index, instance in demoDict.items():
        print(f"{index:2} : {instance.DisplayText}")
    print(f"-1 : Terminate")

def ReadInt() -> int:
    while True:
        try:
            return int(input("\r\nEnter Demo# to run:"))
        except ValueError:
            print("Invalid input. Please enter valid number")
        except KeyboardInterrupt:
            print("\r\nTerminating...!")
            return -1


def RegisterDemo(demo: DemoBase, demoDict: dict):
    instance = demo()
    index = len(demoDict)
    demoDict[index] = instance

demoDict = dict()
demo: DemoBase
for demo in FactoryModule.Factory().demos:
    RegisterDemo(demo, demoDict)

while True:
    PrintAvailableDemos(demoDict)
    userEnteredDemoIndex = ReadInt()
    if userEnteredDemoIndex == -1:
        break
    print('----------------------\r\n')
    demoDict[userEnteredDemoIndex].Demo()
    print('----------------------\r\n')
