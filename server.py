import socket
from init import get_local_ip, get_public_ip
from port_forward import do_udp_port_mapping, do_tcp_port_mapping


def start_udp_server(port):
    do_udp_port_mapping(54321, port)
    LOCAL_IP = get_local_ip()
    PUBLIC_IP = get_public_ip()
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
        )
    sock.bind((LOCAL_IP, port))
    print(f'Waiting for messages on {PUBLIC_IP} : {54321}')
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print(f'received message: {data.decode("utf-8")} from {addr}')


start_udp_server(12345)