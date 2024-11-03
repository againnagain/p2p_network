import socket

def send_pocket_to_peer(msg:bytes, peer_ip:str, peer_port:int):
    
    sock = socket.socket(
        socket.AF_INET, 
        socket.SOCK_DGRAM
        )
    sock.sendto(msg, (peer_ip, peer_port))

peer_ip = input('Enter peer IP: ')
peer_port = int(input('Enter peer port: '))
msg = input('Enter message: ')
send_pocket_to_peer(msg.encode(), peer_ip, peer_port)