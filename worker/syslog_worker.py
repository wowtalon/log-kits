from worker.base_worker import BaseWorker
import socket

class SyslogWorker(BaseWorker):
    def __init__(self, config):
        super().__init__()
        self._target_host, self._target_port = config['target'].split(':')
    
    def process_job(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(data.encode('utf-8'), (self._target_host, int(self._target_port)))
        finally:
            sock.close()