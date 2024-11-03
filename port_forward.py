import time
from init import get_public_ip, get_local_ip, get_port_interface

def do_udp_port_mapping(public_port, local_port):
        PUBLIC_IP = get_public_ip()
        LOCAL_IP = get_local_ip()
        device, interface = get_port_interface()
        service = device[interface]
        service.AddPortMapping(
                NewRemoteHost=PUBLIC_IP,
                NewExternalPort= public_port,
                NewProtocol='UDP',
                NewInternalPort=local_port,
                NewInternalClient=LOCAL_IP,
                NewEnabled=True,
                NewPortMappingDescription=f'net map {time.time()}',
                NewLeaseDuration=600
        )

def do_tcp_port_mapping(public_port, local_port):
        PUBLIC_IP = get_public_ip()
        LOCAL_IP = get_local_ip()
        device, interface = get_port_interface()
        service = device[interface]
        service.AddPortMapping(
                NewRemoteHost=PUBLIC_IP,
                NewExternalPort= public_port,
                NewProtocol='TCP',
                NewInternalPort=local_port,
                NewInternalClient=LOCAL_IP,
                NewEnabled=True,
                NewPortMappingDescription=f'net map {time.time()}',
                NewLeaseDuration=60
        )
