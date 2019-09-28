from netapp_ontap import config
from netapp_ontap import HostConnection
from netapp_ontap.resources import Cluster, Aggregate, Port, Volume, Autosupport, IpInterface, Disk, Chassis, Account, Svm, Snapshot

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

conn = HostConnection('192.168.1.200', username='admin', password='N3tapp1!', verify=False)

config.CONNECTION = conn

name = 'rubrik'
size = 20971520
aggr = 'ntap_study_data'
svm = 'study'

volume = Volume.from_dict({'name': name, 'svm': {'name': svm}, 'nas': {'path': '/'+name} , 'size': size, 'aggregates': [{'name': aggr}]})
volume.post()

vol = Volume.find(name=name)
vol.get(fields='nas.path')
print(vol.nas.path)

"""
#volume = Volume.find(name=name, svm=svm)
#volume.delete()

#for svm in Svm.get_collection():
#    svm.get()
#    print(svm.to_dict())

volumes = []
for vol in Volume.get_collection(svm=svm):
    vol.get(fields='name')
    volumes.append(vol.name)
print(volumes)

aggregates = []
for aggr in Aggregate.get_collection():
    aggr.get(fields='name')
    aggregates.append(aggr.name)
print(aggregates)

ports = []
for port in Port.get_collection():
    port.get()
    ports.append([port.name, port.state])
print(ports)

interfaces = []
for interface in IpInterface.get_collection():
    interface.get()
    interfaces.append([interface.name, interface.state])
print(interfaces)

"""
