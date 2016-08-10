from services import linux

class BaseTemplate:
    name = None
    services = None
    hostname = None
    ip_address = None
    port = None
    os = None

class LinuxGeneralServices(BaseTemplate):
    name = 'Linux General Services'
    services = {
        'cpu':linux.cpu(),
        'memory':linux.memory(),
        'load':linux.load(),
    }
