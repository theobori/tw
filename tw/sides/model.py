"""interface module"""

from enum import Enum
from argparse import ArgumentParser

from exceptions.tw import TwError

class SideType(Enum):
    """
        Representing the different available sides
    """

    SERVER="server"
    CLIENT="client"
    UNKNOWN="unknown"

class Side:
    """
        Model for the different sides
    """
    
    def __init__(self, side: SideType = SideType.UNKNOWN):
        self._side = side
        self._key = None
    
    def set_key(self, key: str):
        """
            Set self._key
        """
        
        self._key = key
    
    def build(self):
        """
            Build the container
        """
        
        raise TwError("Not implemented !")

    def run(self):
        """
            Run the container
        """
        
        raise TwError("Not implemented !")

    @property
    def image(self) -> str:
        """
            Return the Docker image name
        """
    
        return "tw_" + self._side.value + "_" + self._key
    
    @property
    def network(self) -> str:
        """
            Return the Docker network name
        """
        
        return "tw_network" + self._side.value + "_" + self._key

class SideCli(ArgumentParser):
    """
        Model CLI manager
    """
    
    def __init__(self):
        super().__init__()

        self.add_argument(
            "--build",
            action="store_true",
            help="Build the Docker container"
        )
        
        self.add_argument(
            "--run",
            action="store_true",
            help="Run the Docker container"
        )

    def call(self, model: Side):
        """
            Just run...
        """

        raise TwError("Not implemented !")
