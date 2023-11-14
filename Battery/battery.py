from abc import ABC, abstractmethod

class battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass
