from cyder.api.authtoken.models import *
from cyder.base.eav.models import *
from cyder.core.ctnr.models import *
from cyder.core.cyuser.models import *
from cyder.core.system.models import *
from cyder.core.task.models import *
from cyder.cydhcp.interface.dynamic_intr.models import *
from cyder.cydhcp.interface.static_intr.models import *
from cyder.cydhcp.network.models import *
from cyder.cydhcp.range.models import *
from cyder.cydhcp.site.models import *
from cyder.cydhcp.vlan.models import *
from cyder.cydhcp.vrf.models import *
from cyder.cydhcp.workgroup.models import *
from cyder.cydns.address_record.models import *
from cyder.cydns.cname.models import *
from cyder.cydns.cybind.models import *
from cyder.cydns.domain.models import *
from cyder.cydns.mx.models import *
from cyder.cydns.nameserver.models import *
from cyder.cydns.ptr.models import *
from cyder.cydns.soa.models import *
from cyder.cydns.srv.models import *
from cyder.cydns.sshfp.models import *
from cyder.cydns.txt.models import *
from cyder.cydns.view.models import *

MODEL_LIST = [
    Token, Ctnr, UserProfile, System, Task, DynamicInterface,
    StaticInterface, Network, Range, Site, Vlan, Vrf, Workgroup,
    AddressRecord, CNAME, DNSBuildRun, BuildManifest, Domain, MX,
    Nameserver, PTR, SOA, SRV, SSHFP, TXT, View]
