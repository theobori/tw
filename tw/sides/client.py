"""client side module"""

import os

from typing import List, Union

from .model import Side, SideType, SideCli
from exceptions.tw import TwError

HOME_DIR=os.path.expanduser('~')

class UserDirectory:
    """
        Static class
    """
    
    def __userdir(
        appname: str,
        extras_dirs: List[str] = []
    ) -> Union[str, None]:
        """
            Found an user directory
        """

        dirs = [
            HOME_DIR + "/.local/share/." + appname,
            HOME_DIR + "/." + appname,
        ]
        
        if extras_dirs:
            dirs += extras_dirs
            
        for dir in dirs:
            if os.path.exists(dir):
                return dir
        
        return None

    def get(key: str) -> Union[str, None]:
        """
            Public method to get the user directory
        """
        
        default = UserDirectory.__userdir("teeworlds")
        
        if key == "ddnet":
            return default or UserDirectory.__userdir("ddnet")
        
        return default

class Client(Side):
    """
        Client side controller
    """

    def __init__(self):
        super().__init__(SideType.CLIENT)

    @property
    def __userdir(self) -> str:
        """
            Get the user directory
        """
        
        self._key

    def build(self):
        self._build_base()

        self._docker.images.build(
            path=self._key_folder,
            tag=self.image
        )
    
    def __volumes(self) -> list:
        """
            Setup user directory config volumes
        """

        ret = []
        userdir = UserDirectory.get(self._key)

        if not userdir:
            return ret
        
        ret.append(
            userdir + ":" + userdir.replace(
                HOME_DIR,
                "/root"
            )
        )
        
        return ret
    
    def run(self):
        container_id = self._container_last_id + 1
        
        self._docker.containers.run(
            self.image,
            detach=True,
            auto_remove=True,
            name=self.image + str(container_id),
            environment=[
                "DISPLAY=" + os.getenv("DISPLAY")
            ],
            volumes=[
                "/tmp/.X11-unix:/tmp/.X11-unix",
                *self.__volumes()
            ],
            devices=[
                "/dev/snd:/dev/snd",
                "/dev/dri:/dev/dri"
            ]
        )
    
class ClientCli(SideCli):
    """
        Client CLI manager
    """
    
    def __init__(self, client: Client):
        super().__init__(client)
        
        self.__client = client
        self.args = None
        
        self.add_argument(
            "-k", "--key",
            default="teeworlds",
            type=str,
            help="A subfolder name in images/client/"
        )

    def setup(self):
        self.args = self.parse_args()
        
        self.__client.set_key(self.args.key)
        
    def call(self):
        if not self.args:
            raise TwError(
                "The arguments have not been setup !"
            )

        if self.args.list == True:
            self.__client._list()        
        elif self.args.build == True:
            self.__client.build()
        elif self.args.run == True:
            self.__client.run()
        else:
            raise TwError("Missing an action")
