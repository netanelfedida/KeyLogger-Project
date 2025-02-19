from abc import ABC, abstractmethod
from typing import List

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    def stop_logging(self) -> None:
        pass

    def get_logged_keys(self) -> List[str]:
        pass
