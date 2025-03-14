import socket
import yaml


def send_syslog(message, port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), ('127.0.0.1', port))
    print(f"Sent message: {message}")


def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


if __name__ == "__main__":
    # print(read_config("./config.yaml"))
    send_syslog("This is a test message", 5514)