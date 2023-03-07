"""tw main module"""

import argparse

from typing import Any, Dict, Tuple

from sides.model import SideType, Side, SideCli
from sides.server import ServerCli, Server
from exceptions.tw import TwError
# from .sides.client import Client

SideTuple = Tuple[SideCli, Side]

SIDE_LINK: Dict[SideType, SideTuple] = {
    SideType.CLIENT: (ServerCli, Server),
    SideType.SERVER: (ServerCli, Server)
}
IMG_PREFIX="images/"

class Tw:
    """
        Used as the 'main' controller
    """
    
    def __init__(self, side: SideType = SideType.UNKNOWN):
        self.side = side
        
    def __call__(self, *args: Any, **kwds: Any) -> SideTuple:
        if not self.side in SIDE_LINK.keys():
            raise TwError("Invalid side")

        cli, side = SIDE_LINK[self.side]

        # Get the Cli and the Side controller class
        cli = cli()
        side = side()
        
        # Filling and running the Side class
        # with the Cli informations
        cli.call(side)
