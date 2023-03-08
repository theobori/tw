#!/usr/bin/env python

"""main module"""

import docker

from sys import stderr, argv

from exceptions.tw import TwError
from tw import Tw
from sides.model import SideType

class Cli:
    """
        Python create executable module
        Static class containg some cli functions
    """

    def __print_help():
        """
            Print help for the first stage
        """
        
        print("""Usage:
    tw server --help
    tw client --help""")

    def pre_check():
        """
            Checking first stage
        """

        if len(argv) < 2:
            Cli.__print_help()
            exit(1)
        
        if argv[1] in ("-h", "--help"):
            Cli.__print_help()
            exit(0)

def main():
    """
        Module main function
    """
    
    Cli.pre_check()
    
    try:
        side_type = SideType(argv.pop(1)).name
        tw = Tw(SideType[side_type])
        
        tw()
    except Exception as error:
        print(error, file=stderr)
        exit(1)

if __name__ == "__main__":
    main()
