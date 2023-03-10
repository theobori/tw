"""server module"""

import os
import re
import uuid

from .model import Side, SideType, SideCli
from exceptions.tw import TwError

PORT = 8303
DB_DOCKERFILE = "db.dockerfile"

# It will never change
DB_USER = "teeworlds"
DB_PASSWORD = "PW2"
ROOT_PASSWORD = "secret_" + DB_PASSWORD
SQL_CFG = f'''
sv_use_sql 1
add_sqlserver r teeworlds record "root" "{ROOT_PASSWORD}" "%s" "3306"
add_sqlserver w teeworlds record "root" "{ROOT_PASSWORD}" "%s" "3306"
'''

class ServerConf:
    """
        Represents the server configuration
    """
    
    def __init__(self, path: str = ""):
        self.__path = path

    def set_path(self, path: str):
        """
            Set the configuration path
        """
        
        print(path)
        
        if os.path.exists(path) == False:
            raise TwError("Invalid config path")
        
        self.__path = path
    
    @property
    def path(self) -> str:
        """
            Return the path value
        """

        return self.__path
    
    def update_with_sql(
        self,
        host: str,
        sql_cfg: str = SQL_CFG
    ):
        """
            Update the `cfg` server file with
            Dockerfile value (user, password, etc..)
        """
        
        with open(self.__path, "r") as f:
            data = f.read()
            
        cfg_path = "/tmp/" + str(uuid.uuid4()) + ".cfg"
        sql_config = sql_cfg % (host, host)
            
        with open(cfg_path, "a+") as cfg:
            cfg.write(data)
            cfg.write(sql_config)
        
        self.set_path(cfg_path)

class Server(Side):
    """
        Server side controller
    """

    def __init__(self):
        super().__init__(SideType.SERVER)

        self.__port = 8303
        self.config = ServerConf()
        self.with_sql = False

    def set_port(self, port: int):
        """
            Set the server foward port
        """

        self.__port = port

    def __build_network(self):
        """
            Build the Docker network if it doesnt exist
        """

        re_container = re.compile(rf"^{self.network}$")

        networks = list(
            filter(
                lambda c: re_container.fullmatch(c.attrs.get("Name")),
                self._docker.networks.list()
            )
        )
        
        if len(networks) > 0:
            return

        self._docker.networks.create(
            self.network,
            driver="bridge"
        )

    @property
    def __database_name(self) -> str:
        """
            Return the database Docker container name
        """
        
        return self.image + "_db"
    
    def __build_db(self):
        """
            Build the database image
        """
        
        self.__build_network()
        
        self._docker.images.build(
            path=self._key_folder,
            dockerfile=DB_DOCKERFILE,
            tag=self.__database_name
        )

    def __run_db(self):
        """
            Run the database
        """

        image = self.__database_name

        self._docker.containers.run(
            image,
            detach=True,
            auto_remove=True,
            name=image,
            network=self.network,
            environment=[
                f"MARIADB_USER={DB_USER}",
                f"MARIADB_PASSWORD={DB_PASSWORD}",
                f"MARIADB_ROOT_PASSWORD={ROOT_PASSWORD}"
            ]
        )

    def build(self):
        self._build_base()
        
        if self.with_sql:
            self.__build_db()

        self._docker.images.build(
            path=self._key_folder,
            tag=self.image
        )
    
    def clean(self):
        containers = (
            *self._key_containers,
            *self._containers("/" + self.__database_name),
        )
        
        for container in containers:
            container.kill()

    def __volumes(self) -> dict:
        """
            Setup config file(s) volume
        """

        ret = {}
        
        if not self.config.path:
            return ret
    
        ret["volumes"] = [
            self.config.path + ":/server/autoexec.cfg"
        ]
        
        return ret

    def run(self):
        self.__build_network()
        
        if not self.config.path:
            self.config.set_path(
                self._key_folder + "/autoexec.cfg"
            )
        
        container_id = self._container_last_id + 1
        name = self.image + str(container_id)
        
        if self.with_sql:
            self.__run_db()
            self.config.update_with_sql(self.__database_name)
        
        self._docker.containers.run(
            self.image,
            detach=True,
            auto_remove=True,
            name=name,
            ports={str(PORT) + "/udp": [self.__port]},
            network=self.network,
            **self.__volumes()
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
            "-k", "--key",
            default="vanilla",
            type=str,
            help="A subfolder name in images/server/"
        )
        
        self.add_argument(
            "--clean",
            action="store_true",
            help="Kill the instances"
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
            "--with-sql",
            action="store_true",
            help="Use a database as server storage"
        )

        self.add_argument(
            "-c", "--config",
            type=str,
            help="The server absolute cfg path"
        )

        self.add_argument(
            "-p", "--port",
            type=str,
            default=PORT,
            help="The server port"
        )

    def setup(self):
        self.args = self.parse_args()
        
        self.__server.set_key(self.args.key)
        self.__server.set_port(self.args.port)
        
        if (path := self.args.config):
            self.__server.config.set_path(path)

        # self.__server.with_sql = self.args.with_sql

    def call(self):
        if not self.args:
            raise TwError(
                "The arguments have not been setup !"
            )

        if self.args.list == True:
            self.__server._list()        
        elif self.args.build == True:
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
