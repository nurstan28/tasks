class HostError(Exception):
    pass


class Hack:
    def __init__(self, host, ip, port, password):

        # Hack.validate_network_address(host)
        # Hack.validate_network_address(ip)
        # Hack.validate_network_address(port)
        # Hack.validate_network_address(password)

        self.__host = host
        self.__ip = ip
        self.__port = port
        self.__password = password

    @classmethod
    def validate_host(cls, host: str):
        if type(host) != str:
            raise HostError("input value not equal str")

        host = host.split('.')

        if len(host) != 4:
            raise HostError(f'{host} more than 4 elems')

        for ip_section in host:
            if not ip_section.isdigit():
                print(ip_section)
                raise HostError(f"{ip_section} input value not equal str")
            elif 255 > int(ip_section) < 0:
                raise HostError(f"{ip_section} input ip_section more than 255 or less than 0")

    @classmethod
    def validate_ip(cls, ip):
        ips = ip.split(".")
        d = all([True if i.isdigit() else False for i in ips])

        if len(ips) != 4:
            raise TypeError('Incorrect Format')
        if d is False:
            raise TypeError('ip must be digit')
        r = all([True if int(i) in range(0, 256) else False for i in ips])
        if r is False:
            raise TypeError('Should be in range(0,255)')

    @classmethod
    def validate_port(cls, port: str):
        print(port)
        if type(port) != str:
            raise HostError("input value not equal str")

        if len(port) != 2:
            raise HostError("more than 2 elems")

    @classmethod
    def validate_password(cls, password):
        if not password.isdigit():
            raise TypeError('password only digits')

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.validate_ip(ip)
        self.__ip = ip

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.validate_host(host)
        self.__host = host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.validate_port(port)
        self.__port = port

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.validate_password(password)
        self.__password = password

file = open('data.txt', 'r')

lines = file.readlines()
config = dict()

for line in lines:
    key, value = line.split('=')
    config[key.strip()] = value.strip()

hack = Hack(**config)
print(hack.__dict__)





