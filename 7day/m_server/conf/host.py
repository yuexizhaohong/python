import templates
import copy

#for host chu_server
h1 = templates.LinuxGeneralServices()
h1.services = copy.deepcopy(h1.services)
h1.hostname = 'chu_server'
h1.ip_address = '192.168.8.222'
h1.port = 22
h1.os = 'Ubuntu 14.04'
h1.services['cpu'].triggers['iowait'][1] = 80
h1.services['cpu'].triggers['steal'] = ['int',70,75]
h1.services['cpu'].interval = 20
#print h1.services['cpu'].interval
#print h1.services['cpu'].triggers

#for host iotek_server
h2 = templates.LinuxGeneralServices()
h2.services = copy.deepcopy(h2.services)
h2.hostname = 'chu_server'
h2.ip_address = '192.168.8.221'
h2.port = 22
h2.os = 'Centos 6.5'
h2.services['cpu'].triggers['iowait'][1] = 70
del h2.services['load']
#print h1.services['cpu'].triggers,h1.services['cpu'].interval
#print h2.services['cpu'].triggers,h2.services['cpu'].interval


monitored_hosts = [h1,h2]
