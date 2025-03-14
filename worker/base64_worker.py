import base64
from worker.base_worker import BaseWorker

class Base64Worker(BaseWorker):

    def __init__(self, config):
        super().__init__()
        self._command = config['command']

    def encode(self, data: bytes) -> str:
        return base64.b64encode(data).decode('utf-8')

    def decode(self, data: str) -> bytes:
        return base64.b64decode(data)
    
    def process_job(self, data):
        if self._command == 'encode':
            return self.encode(data.encode('utf-8'))
        elif self._command == 'decode':
            return self.decode(data)
        else:
            return f"Unknown base64 action: {self._command}"