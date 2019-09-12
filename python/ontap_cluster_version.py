from netapp_ontap import config
from netapp_ontap import HostConnection
from netapp_ontap.resources import Cluster, Aggregate, Port, Volume, Autosupport, IpInterface, Disk, Chassis, Account, Svm

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

conn = HostConnection('192.168.1.200', username='admin', password='N3tapp1!', verify=False)

config.CONNECTION = conn
clus = Cluster()
clus.get()
print(clus)

aggr = Aggregate.find()
aggr.get()
print(aggr.name, aggr.node)

svm = Svm.find(name = "study")
svm.get()
print(svm.to_dict())