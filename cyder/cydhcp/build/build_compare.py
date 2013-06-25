from functools import total_ordering


class DhcpComparableMixin(object):
    def __eq__(self, other):
        if not isinstnace(self, type(other)):
            raise Exception(
                "Can't comparable incompatable types {0} and {1}".format(
                    type(self), type(other)))
        return self.value() == self.value()

    def value(self):
        pass


class Host(DhcpComparableMixin):
    def __init__(self,
                 fqdn,
                 ip=None,
                 mac=None,
                 options=None,
                 statements=None,
                 classes=None):
        self.fqdn = fqdn
        self.ip = ip
        self.mac = mac
        self.options = options or []
        self.statements = statements or []
        self.classes = classes or []


class Subnet(DhcpComparableMixin):
    ip_class = ipaddr.IPv4Address
    def __init__(self,
                 network_addr,
                 netmask_addr,
                 options=None,
                 statements=None,
                 pools=None,
                 hosts=None):
        self.network_addr = self.ip_class(network_addr)
        self.netmask_addr = self.ip_class(netmask_addr)
        self.options = options or []
        self.statements = statements or []
        self.pools = pools or []
        self.hosts = hosts or []


    def value(self):
        return

class Subnet6(Subnet):
    ip_class = ipaddr.IPv6Address


class Pool(object):
    ip_class = ipaddr.IPv4Address
    def __init__(self,
                 range_start,
                 range_end,
                 hosts=None,
                 subnet=None,
                 options=None,
                 statements=None):
        self.range_start = self.ip_class(range_start)
        self.range_end = self.ip_class(range_end)
        self.subnet = subnet    # Instance of a Subnet class
        self.hosts = hosts or []
        self.options = options or []
        self.statements = statements or []


class Pool6(Pool)
    ip_class = ipaddr.Ipv6Address


class Group(object):
    def __init__(self, options=None, statements=None, hosts=None):
        self.options = options or []
        self.statements = statements or []
        self.hosts = hosts or []


class DhcpClass(object):
    def __init__(name, match):
        self.name = name
        self.match = match

class ConfigTable(object):
    def __init__(self,
