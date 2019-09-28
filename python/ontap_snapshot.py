from netapp_ontap import config
from netapp_ontap import HostConnection
from netapp_ontap.resources import Cluster, Aggregate, Port, Volume, Autosupport, IpInterface, Disk, Chassis, Account, Svm, Snapshot
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

conn = HostConnection('192.168.1.200', username='admin', password='N3tapp1!', verify=False)

config.CONNECTION = conn
#vol = Volume.find(name='movies')
#vol.get()
#print(vol)

#volume = Volume(name='vol1', svm={'name': 'study'}, aggregates=[{'name': 'ntap_study_data'}])
#volume.post()

time = datetime.now()
time = str(time)
volume = Volume.find(name='soccer', svm={'name': 'study'})
volume.get()
snapshot = Snapshot.from_dict({
'name': 'snapshot_%s' % time,
'volume': volume.to_dict(),
})
snapshot.post()