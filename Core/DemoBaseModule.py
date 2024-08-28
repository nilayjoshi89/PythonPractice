from abc import ABC, abstractmethod

class DemoBase(ABC):
    def __init__(self, displayText) -> None:
        self.DisplayText = displayText
        
    @abstractmethod
    def Demo(self):
        raise NotImplementedError