"""client side module"""

import os

from .model import Side, SideType, SideCli
from exceptions.tw import TwError

class Client(Side):
    """
        Client side controller
    """

    def __init__(self):
        super().__init__(SideType.CLIENT)

    def build(self):
        self._build_base()

        self._docker.images.build(
            path=self._key_folder,
            tag=self.image
        )
            
    def run(self):
        self._docker.containers.run(
            self.image,
            tty=True,
            auto_remove=True,
            name=self.image,
            environment=[
                "DISPLAY=" + os.getenv("DISPLAY")
            ],
            volumes=[
                "/tmp/.X11-unix:/tmp/.X11-unix"
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
            "key",
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

        if self.args.build == True:
            self.__client.build()
        elif self.args.run == True:
            self.__client.run()
        elif self.args.clean == True:
            self.__client.clean()
        else:
            raise TwError("Missing an action")
