"""Build or run a Docker image"""

import re
import os

from sys import argv

PORT_RE = re.compile(r"(sv_port)\s+([0-9]+)")

class FngContainer:
    """
        Manages Docker container throught shell commands
    """

    def __init__(self, callback: str, image: str, port: str) -> None:
        callbacks = {
            "build": self.run_and_build,
            "run": self.run
        }

        if not callback in callbacks.keys():
            print("use -h or --help")
            exit(84)

        self.callback = callbacks[callback]
        self.image = image
        self.port = port

    def call(self):
        """
            Executing callback
        """

        self.callback()

    def build(self):
        """
            Build the image
        """

        os.system(f"docker build . -t {self.image}")

    def run(self):
        """
            Run the image into a container
        """

        os.system(f"docker run -it -v $PWD/fng.cfg:/fng2/fng.cfg -p {self.port}:{self.port}/udp {self.image}")

    def run_and_build(self):
        """
            Build + run
        """

        self.build()
        self.run()

def display_cli_help():
    """
        Output help for CLI args
    """

    print("python3 <script> [action] [image_name]")
    print("[action] => build | run")

def args_handler():
    """
        Manages CLI args
    """

    if len(argv) == 2:
        if (argv[1] == "-h" or argv[1] == "--help"):
            display_cli_help()
            exit(0)

    if len(argv) < 3:
        print("use -h or --help")
        exit(84)


def main():
    args_handler()

    with open("fng.cfg", "r") as f:
        content = f.read()
    
    port = PORT_RE.findall(content)[0][1]

    c = FngContainer(*argv[1:], port)
    c.call()

if __name__ == "__main__":
    main()
