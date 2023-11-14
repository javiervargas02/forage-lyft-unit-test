from abc import ABC, abstractmethod

class engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass