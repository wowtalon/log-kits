import lib.workflow
import socket

def listen_syslog(port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    print(f"Listening for syslog messages on port {port}...")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode('utf-8')}")
        lib.workflow.proc_msg(data.decode('utf-8'), "syslog")


def send_syslog(message, host="127.0.0.1", port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (host, port))
    print(f"Sent message: {message}")