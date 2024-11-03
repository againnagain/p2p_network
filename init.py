import socket
import upnpy


def get_port_interface():
    for device in upnpy.UPnP().discover():
        for service in device.get_services():
            if service.id == 'urn:upnp-org:serviceId:WANIPConn1':
                return device, 'WANIPConn1'
            elif service.id == 'urn:schemas-upnp-org:service:WANPPPConn1':
                return device, 'WANPPPConnection.1'
    return Exception('No port mapping interfaces found')

def get_public_ip():
    device, interface = get_port_interface()
    service = device[interface]
    return service.GetExternalIPAddress()

def get_local_ip():
    for hostname in socket.gethostbyname_ex(socket.gethostname()):
        if type(hostname) == str:
            if '192.168' in hostname:
                return ip
        elif type(hostname) == list:
            for ip in hostname:
                if '192.168' in ip:
                    return ip
    return None

