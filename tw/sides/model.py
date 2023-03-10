"""interface module"""

import docker
import re
import os

from enum import Enum
from argparse import ArgumentParser
from os import path
from typing import Union
from sys import stderr

from exceptions.tw import TwError

FILEPATH=os.path.realpath(__file__)
REAL_BASE="/".join(FILEPATH.split("/")[:-3])

IMG_PREFIX=REAL_BASE + "/images"

BASE_DOCKERFILE="base.Dockerfile"

class SideType(Enum):
    """
        Representing the different available sides
    """

    SERVER="server"
    CLIENT="client"
    UNKNOWN="unknown"

class SideBase:
    """
        Virtual pure interface for the `Side` class
        
        This methods will be used with the CLI args
    """

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

    def clean(self):
        """
            Clean
        """
        
        raise TwError("Not implemented !")

    def fclean(self):
        """
            Full clean
        """
        
        raise TwError("Not implemented !")
    
    def re(self):
        """
            `self.fclean` --> `self.build` --> `self.run`
        """
        
        raise TwError("Not implemented !")

class Side(SideBase):
    """
        Model for the different sides
        ~
        Interface + abstract
    """
    
    def __init__(self, side: SideType = SideType.UNKNOWN):
        self._side = side
        self._key = None
        self._docker = docker.from_env()
        self.__base_name = "tw_" + self._side.value

    def __base_dockerfile(self) -> Union[str, None]:
        """
            Return base Dockerfile if exists or `None`
        """
        
        base = self._side_folder + "/" + BASE_DOCKERFILE
        
        if not path.exists(base):
            return None
        
        return base

    def __base_tag(self) -> str:
        """
            Base tag name
        """
        
        return "tw_base_" + self._side.value
    
    def _build_base(self):
        """
            Try to build a potential `base.dockerfile`
        """
        
        if not self.__base_dockerfile():
            return

        self._docker.images.build(
            path=self._side_folder,
            dockerfile=BASE_DOCKERFILE,
            tag=self.__base_tag()
        )
    
    def _containers(self, pattern: str) -> list:
        """
            Return every `Side` containers
        """
        
        # Containers are called with the 
        # same base name as the image name
        re_container = re.compile(rf"{pattern}")
        
        return filter(
            lambda c: re_container.fullmatch(c.attrs.get("Name")),
            self._docker.containers.list()
        )

    @property
    def _key_containers(self) -> list:
        """
            Use `self.containers` with `self.image`
        """

        return self._containers(f"^/{self.image}\d+$")
    
    @property
    def _container_last_id(self) -> int:
        """
            Return the last id created
        """

        containers = list(self._key_containers)

        if len(containers) == 0:
            return 0

        return max(
            map(
                lambda c: int(
                    c.attrs
                        .get("Name")
                        .replace("/" + self.image, "")
                ),
                containers
            )
        )
    
    @property
    def _side_folder(self) -> str:
        """
            Get the folder of the side
        """
    
        return IMG_PREFIX + "/" + self._side.value 
        
    @property
    def _key_folder(self) -> str:
        """
            Get the full path to the folder
        """
        
        if not self._key:
            raise TwError("The key has not been set !")
        
        return self._side_folder + "/" + self._key
    
    def set_key(self, key: str):
        """
            Set self._key
        """
        
        self._key = key
            
        if not path.exists(self._key_folder):
            raise TwError("Invalid key")

    def clean_network(self):
        """
            Remove the network
        """
        
        # for network in self._client.networks.list(
        #     names=[self.network]
        # ):
        #     network.remove()
        
        pass

    def clean(self):
        for container in self._key_containers:
            container.kill()

    def fclean(self):
        self.clean()
        self.clean_network()
        
        # Remove images
        try:
            self._docker.images.remove(
                image=self.image,
                force=True
            )
        except docker.errors.ImageNotFound as error:
            print(error, file=stderr)
    
    def re(self):
        self.fclean()
        self.build()
        self.run()
    
    def _list(self):
        """
            List the availables keys
        """
        
        exclude = (
            "base.Dockerfile",
        )
        
        keys = filter(
            lambda f: not f in exclude,
            os.listdir(self._side_folder)
        )
        
        print("\n".join(keys))

    @property
    def image(self) -> str:
        """
            Return the Docker image tag
        """
        
        if not self._key:
            raise TwError("The key has not been set !")
    
        return self.__base_name + "_" + self._key

    @property
    def network(self) -> str:
        """
            Return the Docker image tag
        """
        
        return self.image
    
class SideCli(ArgumentParser):
    """
        Model CLI manager
    """
    
    def __init__(self, side: Side):
        super().__init__()
        
        self.add_argument(
            "--build",
            action="store_true",
            help="Build (needed before --run)"
        )
        
        self.add_argument(
            "--run",
            action="store_true",
            help="Run"
        )
        
        self.add_argument(
            "-l", "--list",
            action="store_true",
            help="List the availables keys"
        )
    
    def setup(self):
        """
            Setup objects before calling CLI functions
        """
        
        raise TwError("Not implemented !")

    def call(self, model: Side):
        """
            Interact with a `Side` class or child
        """

        raise TwError("Not implemented !")
