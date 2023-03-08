"""server module"""

from .model import Side, SideType, SideCli
from exceptions.tw import TwError

DEFAULT_CONFIG = "server.cfg"
PORT = 8303

class Server(Side):
    """
        Server side controller
    """

    def __init__(self):
        super().__init__(SideType.SERVER)

        self.__port = 8303
        self.__config_path = None
    
    def set_config_path(self, config: str):
        """
            Set the server config path
        """
        
        self.__config_path = config

    def set_port(self, port: int):
        """
            Set the server foward port
        """

        self.__port = port
    
    def build(self):
        self._build_base()

        self._docker.images.build(
            path=self._key_folder,
            tag=self.image
        )
            
    def run(self):
        container_id = self._container_last_id + 1
        name = self.image + str(container_id)
        
        self._docker.containers.run(
            self.image,
            detach=True,
            auto_remove=True,
            name=name,
            ports={PORT: [self.__port]},
        )
    
class ServerCli(SideCli):
    """
        Server CLI manager
    """
    
    def __init__(self, server: Server):
        super().__init__(server)
        
        self.__server = server
        self.args = None
        
        self.add_argument(
            "key",
            type=str,
            help="A subfolder name in images/server/"
        )
        
        self.add_argument(
            "--fclean",
            action="store_true",
            help="Full clean server"
        )

        self.add_argument(
            "--re",
            action="store_true",
            help="'Calling' --fclean --> build --> run server"
        )

        self.add_argument(
            "-c", "--config",
            type=str,
            help="The server cfg path"
        )

        self.add_argument(
            "-p", "--port",
            type=str,
            help="The server port"
        )

    def setup(self):
        self.args = self.parse_args()
        
        self.__server.set_key(self.args.key)
        
        if self.args.port:
            self.__server.set_port(self.args.port)
        
    def call(self):
        if not self.args:
            raise TwError(
                "The arguments have not been setup !"
            )

        if self.args.build == True:
            self.__server.build()
        elif self.args.run == True:
            self.__server.run()
        elif self.args.clean == True:
            self.__server.clean()
        elif self.args.fclean == True:
            self.__server.fclean()
        elif self.args.re == True:
            self.__server.re()
        else:
            raise TwError("Missing an action")
