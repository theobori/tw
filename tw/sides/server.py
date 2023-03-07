"""server module"""

from .model import Side, SideType, SideCli
from exceptions.tw import TwError

class Server(Side):
    """
        Server side controller
    """

    def __init__(self):
        super().__init__(SideType.SERVER)
    
    def build(self):
        return super().build()

    def run(self):
        return super().run()

class ServerCli(SideCli):
    """
        Server CLI manager
    """
    
    def __init__(self):
        super().__init__()
        
        self.add_argument(
            "key",
            type=str,
            help="A subfolder name in images/server/"
        )

    def call(self, server: Server):
        """
            Interact with the `Server` class
            depending of the CLI options
        """
        
        args = self.parse_args()
        
        server.set_key(args.key)
        
        if args.build == True:
            server.build()
        elif args.run == True:
            server.run()
        else:
            raise TwError("Missing an action")
