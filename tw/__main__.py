"""main module"""

from sys import stderr, argv

from exceptions.tw import TwError
from tw import Tw
from sides.model import SideType

def main():
    """
        Module main function
    """

    if len(argv) < 1:
        print("Missing CLI arguments")
        return
    
    # try:
    side_type = SideType(argv.pop(1)).name
    tw = Tw(SideType[side_type])
    
    tw()
    # except TwError as error:
    #     print(error, file=stderr)
    # except Exception as error:
    #     print(error, file=stderr)

if __name__ == "__main__":
    main()
